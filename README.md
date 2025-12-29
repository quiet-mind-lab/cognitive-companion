# 🧠 Cognitive Companion
> *A private space to unload thoughts. Insight over advice. Clarity over comfort.*

![Status](https://img.shields.io/badge/Status-Phase_1_Development-blue)
![Privacy](https://img.shields.io/badge/Privacy-Local_Storage-green)
![Python](https://img.shields.io/badge/Backend-FastAPI-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**Cognitive Companion** is a privacy-first AI system designed to help you gain mental clarity. Instead of acting as a therapist, it acts as a mirror—identifying recurring thoughts and emotional patterns in your daily journal entries over time.

---

## 🎯 Project Scope

This project is built to distinguish between **tool-assisted reflection** and **clinical therapy**.

| ✅ What this project DOES | ❌ What this project does NOT do |
| :--- | :--- |
| **Accepts** daily journaling (Text) | **Therapy** or Counseling |
| **Detects** basic emotional patterns | **Diagnosis** of any condition |
| **Stores** entries privately & locally | **Emotional Roleplay** (chatbotting) |
| **Highlights** recurring themes | **Medical/Psychological Advice** |

---

## 💎 Core Principle

> **"Insight over advice."**
>
> We believe that seeing your thoughts clearly is more powerful than being told what to do. This tool does not "fix" you; it helps you see yourself.

---

## 🛠 Tech Stack

* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Backend:** Python (FastAPI)
* **AI Engine:** TextBlob (Lightweight Sentiment Analysis)
* **Storage:** Local JSON (Privacy-focused)

---

## 🚀 Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone "https://github.com/quiet-mind-lab/cognitive-companion.git"
    cd cognitive-companion
    ```

2.  **Install Backend Dependencies**
    ```bash
    pip install -r backend/requirements.txt
    ```

3.  **Run the Backend**
    ```bash
    fastapi dev backend/main.py
    ```

4.  **Launch the Frontend**
    Open `frontend/index.html` in your browser (or use Live Server).

---

## 🗺 Roadmap

**Phase 1: Foundation (Current)**
- 🟢 Basic Text Journaling Interface
- 🟢 Sentiment Analysis (Positive/Negative/Neutral)
- 🟢 Local Memory Storage (`memory.json`)
- ⚪ Dark Mode UI Polish

**Phase 2: Pattern Recognition**
- ⚪ Weekly Summary Generator
- ⚪ Keyword Extraction (What topics stress you out?)
- ⚪ "On this day" Reflection

**Phase 3: Multi-Modal (Future)**
- ⚪ Voice Note support (Speech-to-Text)
- ⚪ Screenshot Analysis (OCR for notes/chats)

---

## 🔒 Ethics & Privacy
User data is **private by default**.
* No data is sent to third-party AI training servers.
* All memories are stored in `storage/memory.json`.
* You own your data.

---

*Created with ❤️ by [Quiet Mind Labs](https://github.com/quiet-mind-lab) - founder [Deepayan Thakur](https://github.com/Deepayan-Thakur).*
