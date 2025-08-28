# api/v1/answers.py
from fastapi import APIRouter, Depends, HTTPException,Response
from schemas.answer import AnswerResponse
from database.crud import answers_crud
from sqlalchemy.orm import Session
from database.database import get_db
from utils.my_logging import Logging

router = APIRouter()

@router.get("/{answer_id}", response_model=AnswerResponse)
def get_answer(answer_id: int, db: Session = Depends(get_db)) -> AnswerResponse:
    try:
        answer = answers_crud.get_answer_by_id(db, answer_id)
        if not answer:
            raise HTTPException(status_code=404, detail="Answer not found")
        return answer
    except HTTPException as e:
        Logging().log_attention(f"Error when get answer. {e}")
        raise
    except Exception as e:
        Logging().log_attention(f"Error when get answer. {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.delete("/{answer_id}", status_code=204)
def delete_answer(answer_id: int, db: Session = Depends(get_db)) -> Response:
    try:
        deleted = answers_crud.delete_answer(db, answer_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Answer not found")
        return Response(status_code=204)
    except HTTPException as e:
        Logging().log_attention(f"Error when delete answer. {e}")
        raise
    except Exception as e:
        Logging().log_attention(f"Error when delete answer. {e}")
        raise HTTPException(status_code=500, detail="Internal server error")