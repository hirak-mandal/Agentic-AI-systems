from typing import Optional
from pydantic import BaseModel

#request validation 
class ChatRequest(BaseModel):
    message: str
    user_id: str
    session_id: str
    conversation_id: Optional[str]=None
