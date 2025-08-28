from fastapi import APIRouter, Depends, HTTPException,Response
from sqlalchemy.orm import Session
from utils.my_logging import Logging
from database.database import get_db
from typing import Sequence

from fastapi import APIRouter, Depends
from schemas.question import QuestionCreate, QuestionResponse, QuestionWithAnswersResponse
from schemas.answer import AnswerCreate,AnswerResponse
from database.crud import questions_crud, answers_crud
from sqlalchemy.orm import Session
from database.database import get_db

router = APIRouter()

@router.get("/", response_model=Sequence[QuestionResponse])
def list_questions(db: Session = Depends(get_db)) -> Sequence[QuestionResponse]:
    try:
        return questions_crud.get_all_questions(db)
    except HTTPException as e:
        Logging().log_attention(f"Error when get list questions. {e}")
        raise
    except Exception as e:
        Logging().log_attention(f"Error when get list questions. {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
    
@router.post("/", response_model=QuestionResponse)
def create_question(question: QuestionCreate, db: Session = Depends(get_db)) -> QuestionResponse:
    try:
        return questions_crud.create_question(db, text=question.text)
    except HTTPException as e:
        Logging().log_attention(f"Error when post create question. {e}")
        raise
    except Exception as e:
        Logging().log_attention(f"Error when post create question. {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/{question_id}", response_model=QuestionWithAnswersResponse)
def get_question(question_id: int, db: Session = Depends(get_db)) -> QuestionWithAnswersResponse:
    try:
        question = questions_crud.get_question_by_id(db, question_id)
        if not question:
            raise HTTPException(status_code=404, detail="Question not found")
        return question
    except HTTPException as e:
        Logging().log_attention(f"Error when get question. {e}")
        raise
    except Exception as e:
        Logging().log_attention(f"Error when get question. {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.delete("/{question_id}", status_code=204)
def delete_question(question_id: int, db: Session = Depends(get_db)) -> Response:
    try:
        deleted = questions_crud.delete_question(db, question_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Question not found")
        return Response(status_code=204)
    except HTTPException as e:
        Logging().log_attention(f"Error when delete question. {e}")
        raise
    except Exception as e:
        Logging().log_attention(f"Error when delete question. {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/{question_id}/answers", response_model=AnswerResponse)
def create_answer(question_id: int, answer: AnswerCreate, db: Session = Depends(get_db)) -> AnswerResponse:
    try:
        new_answer = answers_crud.create_answer(db, question_id, answer.user_id, answer.text)
        if not new_answer:
            raise HTTPException(status_code=404, detail="Question not found")
        return new_answer
    except HTTPException as e:
        Logging().log_attention(f"Error when create answer. {e}")
        raise
    except Exception as e:
        Logging().log_attention(f"Error when create answer. {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
