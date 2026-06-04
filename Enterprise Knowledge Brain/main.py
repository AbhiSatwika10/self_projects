from fastapi import FastAPI
from backend.rag_pipeline import ask_question

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Enterprise Knowledge Brain Running"}

@app.get("/ask")
def ask(query: str):
    response = ask_question(query)
    return {"response": response}
