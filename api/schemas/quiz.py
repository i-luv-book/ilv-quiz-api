from typing import List, Optional
from pydantic import BaseModel

class QuizOption(BaseModel):
    option: str

class Quiz(BaseModel):
    quiz_num: int
    type: str
    format: str
    question: str
    answer: str
    options: Optional[List[QuizOption]] = None

class QuizList(BaseModel):
    quizzes: List[Quiz]