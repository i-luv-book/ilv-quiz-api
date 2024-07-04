from fastapi import FastAPI, HTTPException, Depends, Body
from .clients.gpt_client import GPTClient

import api.schemas.tale as tale_schema

app = FastAPI()

# GPTClient 
def get_gpt_client():
    return GPTClient()

# 요청 예제
taleInfoExample = {
    "level": "Low/Medium/High-Level",
    "title": "동화 제목",
    "content": "동화 내용"
}

# Responses's Example
quizzesExample = {
    "quizzes": [
        {
            "quiz_num": 1,
            "type": "Reading Comprehension Quiz",
            "format": "True/False",
            "question": "케냐에 특별한 코끼리가 살았어요.",
            "answer": "True"
        },
        {
            "quiz_num": 2,
            "type": "Grammar Quiz",
            "format": "Short Answer",
            "question": "Echo ___ (have) a baby named Ely in 1990.",
            "answer": "had",
            "options": "null"
        },
        {
            "quiz_num": 3,
            "type": "Voca Quiz",
            "format": "Multiple Choice",
            "question": "\"Elephant\"에 맞는 이모티콘을 고르시오.",
            "answer": "C",
            "options": [
                {"option": "🌟"},
                {"option": "🐬"},
                {"option": "🐘"},
                {"option": "🦖"}
            ]
        },
        {
            "quiz_num": 4,
            "type": "Listening Quiz",
            "format": "Short Answer",
            "question": "Listen to the pronunciation and write down the correct answer. \"Ely\"",
            "answer": "Ely",
            "options": "null"
        },
    ]
}

wordsExample = {
    "words": [
        {
            "num": 1,
            "voca": "Elephant",
            "translation": "코끼리"
        },
        {
            "num": 2,
            "voca": "Baby",
            "translation": "아기"
        },
    ]
}

# 퀴즈 생성 API
@app.post("/quizzes", responses={200: {"description": "Successful Response", "content": {"application/json": {"example": quizzesExample}}}})
async def createQuizzes(taleInfo : tale_schema.TaleInfo = Body(..., example=taleInfoExample), gptClient: GPTClient = Depends(get_gpt_client)):
  try:
      return await gptClient.requestQuizzes(taleInfo)
  except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))

# 단어 생성 API
@app.post("/words", responses={200: {"description": "Successful Response", "content": {"application/json": {"example": wordsExample}}}})
async def createWords(taleInfo : tale_schema.TaleInfo = Body(..., example=taleInfoExample), gptClient: GPTClient = Depends(get_gpt_client)):
  try:
      return await gptClient.requestWords(taleInfo)
  except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))