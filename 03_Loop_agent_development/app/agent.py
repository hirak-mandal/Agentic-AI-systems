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
def get_llm_decision(query,history):
    request=client.models.generate_content(
        model="gemini-1.5-flash",
        contents=system_prompt + "\nuser query:" + query + "\nHistory:" + history
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
    history=""
    while True:
        step+=1
        #LLM call
        try:
            llm_output=get_llm_decision(query,history)
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
            continue

        if decision.tool:
                if decision.tool=="weather":
                    tool_result=weather(decision.input)
                elif decision.tool=="sports":
                    tool_result=sports(decision.input)
                #appending history for better context in next iteration
                history+=f"""
                Thought: {decision.hought}
                Action: {decision.tool}
                Observation: {tool_result} 
                """
                continue
        
        if decision.final_answer:
            return decision.final_answer

        if step > max_iteration:
            break
    
