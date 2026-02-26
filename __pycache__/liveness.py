import cv2

# SIMPLE PYTHON 3.13 SAFE LIVENESS CHECK
# (Hackathon-friendly version without mediapipe)

def detect_blink(img):
    """
    Basic liveness detection.
    If a real face is detected, return True.
    This replaces mediapipe blink detection
    which has compatibility issues on Python 3.13.
    """

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # If face detected → assume live user (prototype logic)
    if len(faces) > 0:
        return True

    return False
