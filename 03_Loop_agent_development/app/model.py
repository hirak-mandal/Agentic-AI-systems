from pydantic import BaseModel,model_validator
from typing import Optional,Literal

class Agent(BaseModel):
    tool: Optional[Literal["weather","sports"]]
    final_answer: Optional[str]=None
    input: Optional[str]=None

    #Logical Constraint: checking_existance(Cross-field)
    @model_validator(mode="after")
    def check_one_exists(self):  #one means tool or final_answer
        tool_exists = self.tool
        final_answer_exists= self.final_answer
        input_exists= self.input
        if tool_exists is None and final_answer_exists is None:
            raise ValueError("tool or final_answer must exist") 
        elif tool_exists is not None and final_answer_exists is not None:
            raise ValueError("Between tool and final_answer one should exists")
        elif tool_exists is not None and input_exists is None:
            raise ValueError("Tool exists, then input must exist")
        return self

valid_user=Agent({"tool": "weather", "input": "Kolkata"})
print(valid_user)