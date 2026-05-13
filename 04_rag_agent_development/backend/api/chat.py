from fastapi import APIRouter
from schemas.chat_schema import ChatRequest
from llm.llm_manager import llm_response
#chat.py owns chatbot route
router=APIRouter()

#sending request to backend through POST method
@router.post("/chat")
def logic(request: ChatRequest):
    user_message=request.message
    ai_response=llm_response(user_message)
    return {"reply": ai_response}
