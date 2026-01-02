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
| **Accepts** daily journaling (Text) | **Therapy** or Counseling |
| **Detects** sentiment and intent in entries | **Medical or psychological diagnosis** |
| **Stores** entries privately & locally | **Chatbot roleplay** |
| **Highlights** recurring themes and insights | **Providing advice or treatment** |

---

## 💎 Core Principle

> **"Insight over advice."**  
> We focus on helping users observe their thoughts clearly instead of providing prescriptive solutions. Cognitive Companion does not “fix” you; it helps you see yourself.

---

## 🛠 Tech Stack

* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Backend:** Python (FastAPI)
* **AI Engine:** Embeddings + Sentiment & Intent Analysis
* **Storage:** Local JSON/Index Files (`storage/memory.index`) for semantic search
* **Libraries:** `numpy`, `pydantic`, `fastapi`, `uvicorn`, `scikit-learn` (for embeddings), `textblob` (optional for lightweight sentiment)

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

## 📦 Features

- Daily journaling via web interface  
- Sentiment analysis (POSITIVE / NEGATIVE / MIXED)  
- Intent detection (e.g., venting, reflection)  
- UUID-based entry tracking  
- Local memory storage with semantic search  
- Reflection messages generated for each entry  
- Semantic search by text queries (`/memory/semantic-search`)  
- Retrieve recent entries (`/memory/recent`)

---

## 🗺 Roadmap

**Phase 1: Foundation (Current)**
- 🟢 Basic Text Journaling Interface
- 🟢 Sentiment & Intent Analysis
- 🟢 Semantic Memory Storage (`memory.index`)
- ⚪ Dark Mode UI Polish

**Phase 2: Pattern Recognition**
- ⚪ Weekly Summary Generator
- ⚪ Keyword Extraction & Trending Thoughts
- ⚪ “On this day” Reflection

**Phase 3: Multi-Modal (Future)**
- ⚪ Voice Notes (Speech-to-Text)
- ⚪ Screenshot Analysis (OCR for chats/notes)
- ⚪ Adaptive Insights (AI-driven trends over time)

---

## 🔒 Ethics & Privacy

- User data is **private by default**  
- No data is sent to third-party AI servers  
- All memories are stored locally in `storage/memory.index`  
- You retain **full ownership** of your data  

---

*Created with ❤️ by [Quiet Mind Labs](https://github.com/quiet-mind-lab) — Founder: [Deepayan Thakur](https://github.com/Deepayan-Thakur).*
