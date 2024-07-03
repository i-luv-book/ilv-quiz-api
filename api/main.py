from fastapi import FastAPI, HTTPException, Depends
from .clients.gpt_client import GPTClient

import api.schemas.tale as tale_schema

app = FastAPI()

# GPTClient 
def get_gpt_client():
    return GPTClient()

# 퀴즈 생성 API
@app.post("/quizzes")
async def createQuizzes(taleInfo : tale_schema.TaleInfo, gptClient: GPTClient = Depends(get_gpt_client)):
  try:
      return await gptClient.requestQuizzes(taleInfo)
  except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))

# 단어 생성 API
@app.post("/words")
async def createWords(taleInfo : tale_schema.TaleInfo, gptClient: GPTClient = Depends(get_gpt_client)):
  try:
      return await gptClient.requestWords(taleInfo)
  except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))