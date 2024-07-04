from typing import List
from pydantic import BaseModel

class Word(BaseModel):
  num: int
  voca: str
  translation: str

class WordList(BaseModel):
  words: List[Word]