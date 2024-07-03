import re
from typing import List, Dict, Union

# 응답 퀴즈 데이터 가공
def processQuizList(llmResponse):
  quizzes = llmResponse.split("# Quiz\n")
  splittedQuizzes = splitQuizzes(quizzes[1])
  return parseQuizzes(splittedQuizzes)

def splitQuizzes(data: str):
  # 정규 표현식으로 퀴즈 구분
  pattern = r"(## \d+ - .+?)(?=## \d+ - |\Z)"
  matches = re.findall(pattern, data, re.DOTALL)
  return matches

def parseQuizzes(quiz_data: List[str]) -> List[Dict[str, Union[str, List[str]]]]:
  parsed_data = []
  quiz_pattern = re.compile(r"^\s*## (\d+) - (.+?)\n\s*Question\) (.+?)\n\s*---\n\s*(Options\)\n(.+?)\n\s*---\n\s*)?Answer\) (.+)", re.DOTALL)

  for quiz in quiz_data:
    match = quiz_pattern.search(quiz)
    if match:
      quiz_num = int(match.group(1))
      quiz_type_format = match.group(2)
      question = match.group(3)
      options_block = match.group(4)
      options = match.group(5)
      answer = match.group(6)
      
      # 퀴즈 형식,포맷 분리
      splitted_type_format = quiz_type_format.split('&')
      type = splitted_type_format[0].strip()
      format = splitted_type_format[1].strip() if len(splitted_type_format) > 1 else None
      
      # 파싱
      quiz_dict = {
        "quiz_num": quiz_num,
        "type": type,
        "format": format,
        "question": question.strip(),
        "answer": answer.strip()
      }

      if options:
        # 객관식 문제의 선택지 파싱
        option_lines = options.strip().split('\n')
        quiz_dict["options"] = [opt.strip() for opt in option_lines]

      parsed_data.append(quiz_dict)

  return parsed_data