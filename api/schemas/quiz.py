from typing import List, Optional
from pydantic import BaseModel

class Quiz(BaseModel):
    quiz_num: int
    type: str
    format: str
    question: str
    answer: str
    options: Optional[List[str]] = None

class QuizList(BaseModel):
    quizzes: List[Quiz]