import os
import json
from google import genai
from dotenv import load_dotenv
from app.prompts import system_prompt
from app.model import Agent
from app.tools import weather,sports
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


#agent loop
def run_agent(query):
    step=0
    max_iteration=5
    while True:
        step+=1
        #LLM call
        try:
            llm_output=get_llm_decision(query)
        except Exception as e:
            print(f"Error in LLM call: {e}")
            continue
        #json parsing
        try:
            structured_output=parse_decision(llm_output)
        except Exception as e:
            print(f"Error in json parsing: {e}")
            continue
        #data validation
        try:
            decision=Agent(**structured_output)
            print(decision)
        except Exception as e:
            print(f"Invalid data: {e}")

        if decision.tool:
                if decision.tool=="weather":
                    return weather(decision.input)
                elif decision.tool=="sports":
                    return sports(decision.input)
             
        if decision.final_answer:
            print("\nAnswer:",decision.final_answer)
            break

        if step > max_iteration:
            break
    
