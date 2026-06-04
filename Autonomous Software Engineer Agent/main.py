from fastapi import FastAPI
from backend.orchestrator import execute_task

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Autonomous Software Engineer Agent Running"}

@app.post("/execute")
def execute(task: dict):
    result = execute_task(task["prompt"])
    return {"result": result}
