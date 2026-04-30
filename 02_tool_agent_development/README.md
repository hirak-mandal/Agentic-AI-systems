# Tool Agent 

## 📌 Overview

This project implements a basic AI agent where the LLM acts as a decision-maker.

Based on the user query, the agent decides which tool to use:

* Calculator → for mathematical expressions
* Search → for general queries

## 🧠 Architecture

User Input → LLM → Tool Decision → Tool Execution → Output

## 🚀 Features

* LLM-based decision making
* Modular tool system
* Calculator tool for math operations
* Search tool for general queries
* Structured output validation using Pydantic
* Environment-based API key management

## 🛠️ Tech Stack

* Python
* Gemini API
* Pydantic
* python-dotenv

## 📁 Project Structure

app/
├── main.py
├── agent.py
├── tools/
│    ├── calculator.py
│    └── search.py
├── models/
│    └── schema.py
└── config/
└── settings.py

## ⚙️ Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Create a `.env` file:
   GEMINI_API_KEY=your_api_key_here

3. Run the project:
   python app/main.py

## 🧪 Example

Input:
What is 25 * 4?

Output:
100

---

Input:
Who is Albert Einstein?

Output:
Searched for: Albert Einstein

## 📚 Learnings

* How to use LLMs as decision-makers instead of responders
* Tool-based agent architecture
* Importance of structured validation using Pydantic
* Modular and scalable project design

## 🔮 Future Improvements

* Add more tools (weather, APIs, database queries)
* Replace mock search with real API integration
* Add retry mechanism for invalid LLM outputs
* Multi-step reasoning agents
