from pydantic import BaseModel
from datetime import datetime
from typing import List
from .answer import AnswerResponse

class QuestionCreate(BaseModel):
    text: str

class QuestionResponse(BaseModel):
    id: int
    text: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

class QuestionWithAnswersResponse(BaseModel):
    id: int
    text: str
    created_at: datetime
    answers: List[AnswerResponse] = []

    model_config = {
        "from_attributes": True
    }
