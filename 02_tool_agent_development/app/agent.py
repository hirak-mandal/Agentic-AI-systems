import os
from dotenv import load_dotenv
from google import genai
from app.tools.calculator import calculator
from app.tools.search import search
from app.models.schema import ToolDecision
import json
#load system environment variable
load_dotenv()
#GEMINI API key from environment variable
api_key=os.getenv("GEMINI_API_KEY")

#checking for api crash
if not api_key:
    raise ValueError("API not responding")

#creating client
client=genai.Client(api_key=api_key)

#structured prompt for LLM
system_prompt=system_prompt = """
You are an AI agent that decides which tool to use.

Rules:
- If the query involves math → use "calculator"
- Otherwise → use "search"

Return ONLY valid JSON:
{
  "tool": "calculator" or "search",
  "input": "processed input"
}
"""

#sending request to LLM
def get_LLM_decision(query):
    request=client.models.generate_content(
        model="gemini-1.5-flash",
        contents=system_prompt + "\nuser query" + query
    )
    return request.text

#parse JSON
def parse_decision(response_text):
    try:
        return ToolDecision.model_validate_json(response_text)
    except:
        return ToolDecision(tool="search",input=response_text)
    
#main agent function
def run_agent(query):
    llm_output=get_LLM_decision(query)
    print("RAW LLM:", llm_output)
    decision=parse_decision(llm_output)

    if decision["tool"].lower() == "calculator":
        return calculator(decision["input"])
    else:
        return search(decision["input"])
