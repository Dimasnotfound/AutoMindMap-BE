# backend/app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.nlp import process_text
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AutoMindMap API")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str

@app.post("/process")
async def process(text_input: TextInput):
    try:
        mindmap_data = process_text(text_input.text)
        return {"mindmap": mindmap_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
