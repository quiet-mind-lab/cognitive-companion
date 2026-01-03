# 🧠 Cognitive Companion
> *A private space to unload thoughts. Insight over advice. Clarity over comfort.*

![Status](https://img.shields.io/badge/Status-Phase_1_Development-blue)
![Privacy](https://img.shields.io/badge/Privacy-Local_Storage-green)
![Python](https://img.shields.io/badge/Backend-FastAPI-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**Cognitive Companion** is a privacy-first AI system designed to help you gain mental clarity. Rather than acting as a therapist, it serves as a mirror—identifying recurring thoughts, emotional patterns, and user intent in your daily journal entries over time.

---

## 🎯 Project Scope

This project emphasizes **self-reflection** over therapy or diagnosis.

| ✅ What this project DOES | ❌ What this project does NOT do |
| :--- | :--- |
| **Accepts** daily journaling (text) | **Therapy** or Counseling |
| **Detects** sentiment (POSITIVE / NEGATIVE / MIXED) and intent | **Medical or psychological diagnosis** |
| **Stores** entries privately & locally | **Chatbot roleplay** |
| **Highlights** recurring themes and weekly insights | **Providing advice or treatment** |

---

## 💎 Core Principle

> **"Insight over advice."**  
> Cognitive Companion helps users observe their thoughts clearly rather than providing prescriptive solutions. It does not “fix” you; it helps you see yourself.

---

## 🛠 Tech Stack

* **Frontend:** HTML5, CSS3, Vanilla JavaScript  
* **Backend:** Python (FastAPI)  
* **AI Engine:** HuggingFace `transformers` (sentiment) + `sentence-transformers` (embeddings)  
* **Storage:** Local JSON + FAISS index (`storage/memory.index`) for semantic search  
* **Libraries:** `numpy`, `pydantic`, `fastapi`, `uvicorn`, `faiss-cpu`, `sentence-transformers`

---

## 🚀 Installation & Setup

1. **Clone the repository**
    ```bash
    git clone https://github.com/quiet-mind-lab/cognitive-companion.git
    cd cognitive-companion
    ```

2. **Install Backend Dependencies**
    ```bash
    pip install -r backend/requirements.txt
    ```

3. **Run the Backend**
    ```bash
    uvicorn backend.main:app --reload
    ```

4. **Launch the Frontend**
    Open `frontend/index.html` in your browser (or use Live Server).

---

## 📦 Features (Currently Implemented)

- Daily journaling via web interface (`/journal/text`)  
- Sentiment analysis (POSITIVE / NEGATIVE / MIXED)  
- Intent detection (venting, reaction, reflection, affirmation)  
- UUID-based entry tracking  
- Local memory storage with **semantic search** (`/memory/semantic-search`)  
- Retrieve recent entries (`/memory/recent`)  
- Weekly cognition summary (`/cognition/weekly`) with emotional stability, dominant intents, entry count, and confidence score  

**Phase 2 features (planned but partially implemented in backend modules):**  
- Emotion trends, theme extraction, and reflection synthesis  

---

## 🗺 Roadmap

**Phase 1: Foundation (Completed/Current)**
- 🟢 Journaling Interface & API endpoints  
- 🟢 Sentiment & Intent Analysis  
- 🟢 Local Memory Storage (`memory.json` + `memory.index`)  
- 🟢 Weekly Summary (`/cognition/weekly`)  
- ⚪ Frontend UI polish  

**Phase 2: Pattern Recognition (Backend modules exist, API endpoints in progress)**
- ⚪ Emotional trends over time  
- ⚪ Keyword & theme extraction  
- ⚪ Reflection synthesis  

**Phase 3: Multi-Modal (Future)**
- ⚪ Voice Notes (Speech-to-Text)  
- ⚪ Screenshot Analysis (OCR for notes)  
- ⚪ Adaptive Insights (AI-driven trends over time)  

---

## 🔒 Ethics & Privacy

- All user data is **private by default**  
- No data is sent to external AI servers  
- Memories are stored locally (`memory.json` + `memory.index`)  
- Users retain **full ownership** of their data  

---

*Created with ❤️ by [Quiet Mind Labs](https://github.com/quiet-mind-lab) — Founder: [Deepayan Thakur](https://github.com/Deepayan-Thakur)*
