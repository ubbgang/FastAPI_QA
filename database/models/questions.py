from sqlalchemy import Integer, String, DateTime,func
from sqlalchemy.orm import Mapped,mapped_column,relationship
from datetime import datetime
from .base import Base

class Question(Base):
    '''
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)\n
    text: Mapped[str] = mapped_column(String, nullable=False)\n
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), server_default=func.now())
    '''
    __tablename__ = 'questions'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now(), server_default=func.now())
    
    answers = relationship("Answer",back_populates="question",cascade="all, delete-orphan")