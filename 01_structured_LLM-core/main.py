import os
from dotenv import load_dotenv
from google import genai
#load environment variables from .env file
load_dotenv()

#taking api key from environment variable
api_key=os.getenv("GEMINI_API_KEY")

#checking API key failure
if not api_key:
      raise ValueError("API key not found. Please set the GEMINI-API-KEY environment variable.")

#create client
client=genai.Client(api_key=api_key)

#user input
user_input=input("Enter your prompt:")

#create structured prompt
prompt=f"""
Return ONLY valid JSON in this format:

{{
  "topic": "...",
  "summary": "...",
  "keywords": ["...", "..."]
}}

Input: {user_input}
"""

try:
    #send request to the API
    response=client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
          )
    print("\nresponse\n:")

    #answer
    print(response.text)


except Exception as e:
        print("An error occurred while communicating with the GEMINI API:")
        print("Error:",e)

'''
API KEY FAILING SO PROJECT IS COMPLETED WITH JSON(FOR NOW FOCUS ON LOGIC & STRUCTURE)
              Daily free qutoa of API key limit=0
______________________________________________________________________________________

import json

def mock_llm():
    return """
    {
      "topic": "Robotics",
      "summary": "Robotics is the field of engineering focused on designing and building robots.",
      "keywords": ["robots", "automation", "AI"]
    }
    """
response_text = mock_llm()
# Parse JSON
try:
    data = json.loads(response_text)

    print("\nParsed Output:\n")
    print("Topic:", data["topic"])
    print("Summary:", data["summary"])
    print("Keywords:", data["keywords"])

except json.JSONDecodeError:
    print("Invalid JSON format")



'''