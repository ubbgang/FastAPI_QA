from sqlalchemy.orm import Session
from sqlalchemy import select,delete
from database.models import Answer, Question
from typing import List
import uuid

def create_answer(db: Session, question_id: int, user_id: uuid.UUID, text: str) -> Answer | None:
    question = db.execute(select(Question).where(Question.id == question_id)).scalar_one_or_none()
    if not question:
        return None

    new_answer = Answer(question_id=question_id, user_id=user_id, text=text)
    db.add(new_answer)
    db.commit()
    db.refresh(new_answer)
    return new_answer

def get_answer_by_id(db: Session, answer_id: int) -> Answer | None:
    result = db.execute(select(Answer).where(Answer.id == answer_id))
    return result.scalar_one_or_none()

def get_answers_by_question(db: Session, question_id: int) -> List[Answer]:
    result = db.execute(select(Answer).where(Answer.question_id == question_id))
    return list(result.scalars().all())

def delete_answer(db: Session, answer_id: int) -> bool:
    result = db.execute(delete(Answer).where(Answer.id == answer_id))
    db.commit()
    is_deleted = not (result.rowcount == 0)
    return is_deleted


