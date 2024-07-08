from fastapi import FastAPI, HTTPException, Depends, Body
from .clients.gpt_client import GPTClient
from fastapi.middleware.cors import CORSMiddleware

import api.schemas.tale as tale_schema

app = FastAPI()

# CORS 설정
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # 접근 허용할 도메인 지정
    allow_credentials=True,    # 인증 정보(쿠키 등)를 허용할지 여부를 설정
    allow_methods=["*"],       # 허용할 HTTP 메서드를 지정, 여기서는 모든 메서드 허용
    allow_headers=["*"],       # 허용할 HTTP 헤더를 지정, 여기서는 모든 헤더 허용
)

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
            "quiz_type": "Reading Comprehension Quiz",
            "format": "True/False",
            "question": "에코라는 코끼리가 아기를 두고 떠났어요.",
            "pronunciation_or_voca": "null",
            "options": "null",
            "answer": "False"
        },
        {
            "quiz_num": 3,
            "quiz_type": "Voca Quiz",
            "format": "Multiple Choice",
            "question": "다음 단어에 맞는 이모티콘을 고르세요.",
            "pronunciation_or_voca": "Elephant",
            "options": [
                "🐘",
                "🐬",
                "🦖",
                "😀"
            ],
            "answer": "A"
        },
        {
            "quiz_num": 10,
            "quiz_type": "Creativity Quiz",
            "format": "Short Answer",
            "question": "엘리와 같이 멋진 코끼리가 되어 무엇을 해보고 싶나요?",
            "pronunciation_or_voca": "null",
            "options": "null",
            "answer": "null"
        }
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