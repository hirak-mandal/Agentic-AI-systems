# Structured LLM Core

## 📌 Overview

This project demonstrates how to build a structured interaction layer with an LLM.
Instead of relying on free-form text, the system enforces structured outputs (JSON), making responses predictable and reliable.

## 🚀 Features

* Structured JSON output from LLM
* Prompt engineering for controlled response
* Clean modular design

## 🛠️ Tech Stack

* Python
* Gemini API

## ⚙️ Setup

1. Clone the repository

2. Install dependencies:
   pip install -r requirements.txt

3. Create a `.env` file:
   GEMINI_API_KEY=your_api_key_here

4. Run the project:
   python app/main.py

## 🧪 Example

Input:
"What is 10 * 5?"

Output:
{
"question": "What is 10 * 5?",
"answer": 50
}

## 📚 Learnings

* Importance of structured outputs in LLM systems
* Handling unreliable model responses
* Building foundation for AI agents

## 🔮 Future Improvements

* Better validation and retry mechanisms
* Integration with external APIs
* Multi-step reasoning
