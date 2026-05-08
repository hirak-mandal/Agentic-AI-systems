# Loop Agent

## 📌 Overview

This project implements a ReAct-style AI Agent using a Thought → Action → Observation loop.

The agent uses an LLM as a reasoning engine. Based on the user query, the LLM decides whether to:

* Call a tool
* Observe the tool result
* Continue reasoning
* Return the final answer

The project demonstrates the foundational architecture behind modern Agentic AI systems.

---

## 🧠 Architecture

User Query → LLM Reasoning → Tool Decision → Tool Execution → Observation → Re-Reasoning → Final Answer

---

## 🚀 Features

* ReAct-style agent loop
* Thought → Action → Observation workflow
* LLM-based decision making using Gemini
* Tool calling architecture
* Structured JSON outputs
* Pydantic-based response validation
* Conversation history tracking
* Modular and scalable code structure
* Environment-based API key management

---

## 🛠️ Tech Stack

* Python
* Gemini API
* Pydantic
* python-dotenv
* os
* json
---

## 📁 Project Structure

03_Loop_agent_development/
├── app/
│    ├── agent.py
│    ├── model.py
│    ├── prompts.py
│    ├── tools.py
│
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── main.py

---

## ⚙️ Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Create a `.env` file:
   GEMINI_API_KEY=your_api_key_here

3. Run the project:
   python main.py

---

## 🧪 Example

Input:
What is the weather in Kolkata?

LLM Output:
{
    "thought":"I need weather information",
    "tool":"weather",
    "input":"Kolkata"
}

Observation:
Weather in Kolkata is 32°C humid

Final Output:
{
    "thought":"I now have enough information",
    "final_answer":"Weather in Kolkata is 32°C humid"
}

---

## 📚 Learnings

* How ReAct-style AI agents work internally
* Difference between parsing and validation
* Tool calling workflows in AI agents
* Agent memory and history handling
* Multi-step reasoning loops
* Structured output generation using JSON
* Pydantic validation for reliable agent outputs
* Modular AI system architecture

---

## 🔮 Future Improvements

* Real Weather API integration
* Tool registry pattern
* FastAPI backend integration
* RAG-based memory systems
* Vector database integration
* Multi-tool reasoning
* LangChain / LangGraph integration
* Docker deployment support

---

## ⭐ Project Status

✅ Completed — Version 1 Loop Agent