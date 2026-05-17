# RAG AI Backend

## 📌 Overview

This project is a Retrieval-Augmented Generation (RAG) AI backend built using:

- FastAPI
- FAISS
- Sentence Transformers
- Google Gemini API

The system retrieves relevant information from local text documents using semantic search and generates grounded AI responses using Gemini.

---

# 🚀 Features

- Semantic document retrieval
- Text chunking pipeline
- Embedding generation
- FAISS vector search
- Gemini-powered response generation
- FastAPI backend API
- Modular project architecture

---

# 🧠 Architecture

```text
User Query
    ↓
FastAPI Route
    ↓
Retriever
    ↓
FAISS Vector Search
    ↓
Relevant Chunks
    ↓
Prompt Injection
    ↓
Gemini Response
    ↓
API Response

# 📂 Project Structure

```text
backend/
│
├── api/
│   └── chat.py
│
├── core/
│   └── prompts.py
│
├── llm/
│   ├── gemini_client.py
│   └── llm_manager.py
│
├── rag/
│   ├── text_chunker.py
│   ├── embedder.py
│   ├── faiss_store.py
│   ├── retriever.py
│   └── pipeline.py
│
├── schemas/
│   └── chat_schema.py
│
├── utils/
│   └── file_loader.py
│
├── data/
│   └── knowledge_base/
│
├── .env
├── requirements.txt
└── main.py
```

---

# ⚙️ Technologies Used

- Python
- FastAPI
- FAISS
- Sentence Transformers
- Google Gemini API
- Hugging Face Embeddings

---

# 📦 Installation

## 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd backend
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

---

## 3️⃣ Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

# ▶️ Run Vector Pipeline

This creates embeddings and stores vectors in FAISS.

```bash
python -m rag.pipeline
```

---

# ▶️ Run Backend Server

```bash
uvicorn main:app --reload
```

---

# 🧪 API Testing

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Example request:

```json
{
  "user_id":"123",
  "session_id":"abc",
  "message":"When does NEET batch start?"
}
```

---

# 📚 How RAG Works

1. Documents are loaded from local files.
2. Documents are split into chunks.
3. Chunks are converted into embeddings.
4. Embeddings are stored in FAISS.
5. User query is embedded.
6. FAISS retrieves similar chunks.
7. Retrieved chunks are injected into the prompt.
8. Gemini generates grounded answers.

---

# 🔥 Example Response

```json
{
  "reply": "The NEET Biology special batch starts at 4:00 PM on weekdays."
}
```

---

# 📈 Future Improvements

- Conversation memory
- Persistent vector database
- Streaming responses
- Frontend integration
- Authentication system
- Hybrid search
- Reranking

---

# 👨‍💻 Author

Hirak Mandal