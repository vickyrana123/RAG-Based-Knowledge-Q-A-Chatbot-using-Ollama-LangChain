from fastapi import FastAPI
from pydantic import BaseModel
from rag import chatbot_ask

app = FastAPI(title="RAG Chatbot using Ollama")

class Question(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "RAG Chatbot API is running"}

@app.post("/ask")
def ask(question: Question):
    answer = chatbot_ask(question.question)
    return {
        "question": question.question,
        "answer": answer
    }
