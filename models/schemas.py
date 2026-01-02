from pydantic import BaseModel
from typing import Optional

class ComplaintRequest(BaseModel):
    message: str

class AgentResponse(BaseModel):
    action: str
    reply: str
    case_id: Optional[str] = None
    priority: Optional[str] = None
    escalated: Optional[bool] = None #true ya false