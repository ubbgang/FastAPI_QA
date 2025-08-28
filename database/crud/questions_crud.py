from sqlalchemy.orm import Session,joinedload
from sqlalchemy import select,delete
from database.models import Question

def create_question(db: Session, text: str) -> Question:
    new_question = Question(text=text)
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question

def get_all_questions(db: Session) -> list[Question]:
    result = db.execute(select(Question))
    return list(result.scalars().all())

def get_question_by_id(db: Session, question_id: int) -> Question | None:
    question = (
    db.query(Question)
    .options(joinedload(Question.answers))
    .filter(Question.id == question_id)
    .first()
    )
    return question

def delete_question(db: Session, question_id: int) -> bool:
    result = db.execute(delete(Question).where(Question.id == question_id))
    db.commit()
    is_deleted = not (result.rowcount == 0)
    return is_deleted
        
        
