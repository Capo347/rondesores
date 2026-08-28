from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from ai import ask_ai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://rondesores.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

memory = []

@app.get("/")
def home():
    return FileResponse("index.html")

from pydantic import BaseModel

class Question(BaseModel):
    question: str

    @app.post("/ask")
    def ask(data: dict):
        answer = ask_ai(data["question"], "", memory)
        return{"answer": answer}