import os
from google import genai
from dotenv import load_dotenv

#system environment variable loading
load_dotenv()
#API key
api_key=os.getenv("GEMINI_API_KEY")
#API key checking
if not api_key:
    raise ValueError("API key not responding!!!")
#creating GEMINI client
client=genai.Client(api_key=api_key)
