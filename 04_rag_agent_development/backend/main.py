from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
#creating FastAPI application/server instance
app=FastAPI()

#request validation 
class ChatRequest(BaseModel):
    message: str
    user_id: str
    session_id: str
    conversation_id: Optional[str]=None

#sending request to backend through POST method
@app.post("/chat")
def logic(request: ChatRequest):
    user_message=request.message
    return f"I've received your message:{user_message}"
    