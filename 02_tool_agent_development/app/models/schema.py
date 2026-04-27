from pydantic import BaseModel
from typing import Literal

class ToolDecision(BaseModel):
    tool: Literal["calculator","search"]
    title: str