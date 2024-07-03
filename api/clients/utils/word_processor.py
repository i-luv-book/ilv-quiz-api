import re
from typing import List, Dict

# 응답 단어 데이터 가공
def processWordList(llmResponse):
  splittedWords = splitWords(llmResponse)
  return parseWords(splittedWords)

def splitWords(data: str):
  return data.split("# Words\n")[1]

def parseWords(data: str) -> List[Dict[str, str]]:
  word_list = []
  pattern = re.compile(r"(\d+)\.\s*(\w+)\s*:\s*(.+)")
  
  # 각 줄을 검사하여 패턴 매칭
  for line in data.strip().split('\n'):
    match = pattern.match(line.strip())
    if match:
      word_number = int(match.group(1))
      word = match.group(2)
      translation = match.group(3)
      word_list.append({
          "word_number": word_number,
          "word": word,
          "translation": translation
      })
  
  return word_list