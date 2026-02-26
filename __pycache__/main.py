from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import cv2

from utils.image_utils import bytes_to_image
from face_auth import simple_face_match
from liveness import detect_blink
from risk_engine import evaluate_risk

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/verify")
async def verify(file: UploadFile = File(...)):

    content = await file.read()
    img = bytes_to_image(content)

    # Face detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades+'haarcascade_frontalface_default.xml'
    )

    faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=3,
    minSize=(60,60)
)
    if len(faces)==0:
        return {"status":"NO_FACE","risk":"HIGH"}

    match = simple_face_match(img)
    blink = detect_blink(img)

    status, risk = evaluate_risk(match, blink)

    return {
        "status":status,
        "risk":risk,
        "blink":blink,
        "face_match":match
    }
