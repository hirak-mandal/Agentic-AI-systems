from llm.gemini_client import client
from core.prompts import system_prompt
def llm_response(query):
    response=client.models.generate_content(
        model="gemini-1.5-flash",
        contents=system_prompt + query
    )
    return response.text