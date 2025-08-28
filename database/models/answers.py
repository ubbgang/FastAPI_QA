from sqlalchemy import Integer, String, DateTime,func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import Mapped,mapped_column,relationship
from datetime import datetime
from .base import Base
from .questions import Question

class Answer(Base):
    '''
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)\n
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey(Question.id, ondelete="CASCADE"), nullable=False)\n
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)\n
    text: Mapped[str] = mapped_column(String, nullable=False)\n
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), server_default=func.now())
    '''
    __tablename__ = 'answers'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey(Question.id, ondelete="CASCADE"), nullable=False)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    text: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), server_default=func.now())
    
    question = relationship("Question", back_populates="answers")