from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from transformers import pipeline
import json
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    framework="pt"
)
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_FILE = os.path.join(BASE_DIR, "storage", "memory.json")

class JournalEntry(BaseModel):
    text: str

def save_memory(entry):
    try:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(entry)

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.post("/journal/text")
def journal_text(entry: JournalEntry):
    try:
        result = sentiment_model(entry.text)
        sentiment = result[0]
    except Exception as e:
        sentiment = {
            "label": "ERROR",
            "score": 0.0,
            "error": str(e)
        }

    record = {
        "type": "text",
        "content": entry.text,
        "sentiment": sentiment,
        "timestamp": datetime.utcnow().isoformat()
    }

    save_memory(record)
    return record
