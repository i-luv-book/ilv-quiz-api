import httpx
import api.schemas.tale as tale_schema
import api.clients.utils.word_processor as wordsProcessor
import api.clients.utils.quiz_processor as quizzesProcessor

from api.clients.prompts.quiz_prompt import quizPromptGenerator
from api.clients.prompts.word_prompt import wordPromptGenerator
from ..config import settings

class GPTClient:
  # OpenAPI 설정
  def __init__(self):
    self.wordModel = settings.OPENAI_WORD_MODEL
    self.apiKey = settings.OPENAI_API_KEY
    self.endpoint = "https://api.openai.com/v1/chat/completions"
    self.headers = {
        "Authorization": f"Bearer {self.apiKey}",
        "Content-Type": "application/json"
    }
    
  # 퀴즈 요청  
  async def requestQuizzes(self, taleInfo : tale_schema.TaleInfo):
    quizSystemPrompt = quizPromptGenerator.generateQuizSystemPrompt()
    quizUserPrompt = quizPromptGenerator.processQuizUserPrompt(taleInfo)  # 프롬프트 가공
    
    response = await self.get_completion(settings.OPENAI_QUIZ_MODEL, quizSystemPrompt, quizUserPrompt)  #  응답 가공, TODO: 2024/07/09 파인튜닝된 모델로 변경하기
    return quizzesProcessor.processQuizList(response)
  
  # 단어장 요청
  async def requestWords(self, taleInfo : tale_schema.TaleInfo):
    wordSystemPrompt = wordPromptGenerator.generateWordSystemPrompt()
    wordUserPrompt = wordPromptGenerator.processWordUserPrompt(taleInfo)  # 프롬프트 가공
   
    response = await self.get_completion(settings.OPENAI_WORD_MODEL, wordSystemPrompt, wordUserPrompt)   # 응답 가공
    return wordsProcessor.processWordList(response) 
  
  
  # GPT 요청
  async def get_completion(self, model: str, system_prompt: str, user_prompt: str):
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    }
    async with httpx.AsyncClient(timeout=None) as client:
        response = await client.post(self.endpoint, headers=self.headers, json=data)
        response.raise_for_status()
        completion = response.json()
        return completion["choices"][0]["message"]["content"].strip()