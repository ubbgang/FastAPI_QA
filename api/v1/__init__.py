from fastapi import APIRouter,Depends
from .questions import router as questions_router
from .answers import router as answers_router

router = APIRouter()
router.include_router(questions_router, prefix="/questions", tags=["Questions"])
router.include_router(answers_router, prefix="/answers", tags=["Answers"])

    