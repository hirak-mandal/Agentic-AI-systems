import os
from dotenv import load_dotenv
from openai import OpenAI
#load environment variables from .env file
load_dotenv()

#taking api key from environment variable
api_key=os.getenv("OPENAI-API-KEY")

#creating an instance of OpenAI client
client=OpenAI(api_key=api_key)

#user input
user_input=input("Enter your prompt:")

#sending request to OpenAI LLM
response= client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"user","content":user_input}
    ]
)

#response
print("/nresponse/n:")

#answer
print(response.choices[0].message.content)

