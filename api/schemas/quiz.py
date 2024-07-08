from typing import List, Optional
from pydantic import BaseModel

class Quiz(BaseModel):
    quiz_num: int
    quiz_type: str
    format: str
    question: str
    pronunciation_or_voca: Optional[str] = None
    options: Optional[List[str]] = None
    answer: Optional[str] = None

class QuizList(BaseModel):
    quizzes: List[Quiz]