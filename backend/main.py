from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from datetime import datetime
import uuid
import json
import os

# -------------------------
# App setup
# -------------------------
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

# -------------------------
# Models
# -------------------------
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    framework="pt"
)

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
EMBEDDING_DIM = 384

# -------------------------
# Storage
# -------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STORAGE_DIR = os.path.join(BASE_DIR, "storage")
os.makedirs(STORAGE_DIR, exist_ok=True)

MEMORY_FILE = os.path.join(STORAGE_DIR, "memory.json")
FAISS_INDEX_FILE = os.path.join(STORAGE_DIR, "memory.index")

if os.path.exists(FAISS_INDEX_FILE):
    index = faiss.read_index(FAISS_INDEX_FILE)
else:
    index = faiss.IndexFlatL2(EMBEDDING_DIM)

if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        json.dump([], f)

# -------------------------
# Request model
# -------------------------
class JournalEntry(BaseModel):
    text: str

# -------------------------
# Cognitive helpers
# -------------------------
def detect_mixed_emotion(text: str) -> bool:
    return any(k in text.lower() for k in ["but", "however", "although", "yet"])

def detect_intent(text: str) -> str:
    t = text.lower()
    if any(w in t for w in ["feel", "overwhelmed", "stressed"]):
        return "venting"
    if any(w in t for w in ["angry", "not acceptable"]):
        return "reaction"
    if any(w in t for w in ["amazing", "great", "nice"]):
        return "affirmation"
    return "reflection"

def generate_reflection(intent: str, sentiment: dict) -> str:
    if intent == "venting" and sentiment.get("mixed"):
        return "You seem to be holding conflicting feelings. That’s completely human."
    if sentiment["label"] == "NEGATIVE":
        return "This sounds difficult. You don’t need to solve it right now."
    if sentiment["label"] == "POSITIVE":
        return "There’s something positive here. Notice what led to this feeling."
    return "Thanks for taking a moment to write this down."

def load_memory():
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

# -------------------------
# API Endpoints
# -------------------------
@app.post("/journal/text")
def journal_text(entry: JournalEntry):
    sentiment_result = sentiment_model(entry.text)[0]
    sentiment_result["mixed"] = detect_mixed_emotion(entry.text)

    intent = detect_intent(entry.text)
    reflection = generate_reflection(intent, sentiment_result)

    embedding = embedding_model.encode(entry.text).astype("float32")

    record = {
        "id": str(uuid.uuid4()),
        "type": "text",
        "content": entry.text,
        "embedding": embedding.tolist(),   # 🔥 STORED
        "sentiment": sentiment_result,
        "intent": intent,
        "reflection": reflection,
        "timestamp": datetime.utcnow().isoformat()
    }

    # ---- Persist ----
    memory = load_memory()
    memory.append(record)
    save_memory(memory)

    index.add(np.array([embedding]))
    faiss.write_index(index, FAISS_INDEX_FILE)

    response = record.copy()
    response.pop("embedding", None)
    return response


@app.post("/memory/semantic-search")
def semantic_search(query: JournalEntry, top_k: int = 3):
    if index.ntotal == 0:
        return []

    query_embedding = embedding_model.encode(query.text).astype("float32")
    distances, indices = index.search(np.array([query_embedding]), top_k)

    memory = load_memory()

    results = []
    for idx in indices[0]:
        if 0 <= idx < len(memory):
            results.append({
                "id": memory[idx]["id"],
                "content": memory[idx]["content"],
                "score": float(distances[0][list(indices[0]).index(idx)]),
                "timestamp": memory[idx]["timestamp"]
            })

    return results

@app.get("/memory/recent")
def get_recent_entries(limit: int = 5):
    memory = load_memory()
    return memory[-limit:]
