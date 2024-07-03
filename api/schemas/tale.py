from pydantic import BaseModel, Field

# 동화 및 레벨 정보
class TaleInfo(BaseModel):
  level: str = Field(None, exmaple = "Low-Level")
  title: str = Field(None, exmaple = "제목1")
  content: str = Field(None, exmaple = "내용1")