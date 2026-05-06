import os
import json
from google import genai
from dotenv import load_dotenv
from app.prompts import system_prompt
from app.model import Agent

#loading system environment variables
load_dotenv()

#parsing API KEY from environment variable
api_key=os.getenv("GEMINI_API_KEY")

#checking API KEY 
if not api_key:
    raise ValueError("API KEY not responding......")

#creating client
client=genai.Client(api_key=api_key)

#LLM Call
def get_llm_decision(query):
    request=client.models.generate_content(
        model="gemini-1.5-flash",
        contents=system_prompt + "\nuser query:" + query
    )
    return request.text

#JSON parsing
def parse_decision(response_text):
    data=json.loads(response_text)
    return data

#response validation
def data_validation(data):
    return Agent.model_validate_json(data)

#agent loop
step=0
max_iteration=5
while True:
    step+=1
    llm_output=get_llm_decision()
    structured_output=parse_decision(llm_output)
    decision=data_validation(structured_output)
    if step > max_iteration:
        break
    
