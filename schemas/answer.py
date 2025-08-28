from pydantic import BaseModel
from datetime import datetime
import uuid

class AnswerCreate(BaseModel):
    user_id: uuid.UUID
    text: str

class AnswerResponse(BaseModel):
    id: int
    question_id: int
    user_id: uuid.UUID
    text: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
