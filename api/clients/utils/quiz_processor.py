import re
import api.schemas.quiz as quiz_schema

# 응답 퀴즈 데이터 가공
def processQuizList(llmResponse):
  return parseQuiz(llmResponse)

# 객관식 파싱
def parseOption(data) :
  options = []

  optionBlocks = data.split("|")
  for block in optionBlocks:
    options.append(block.strip().split(". ")[1])

  return options

# 퀴즈 파싱
def parseQuiz(data):
  pattern = re.compile(
    r'^\s*## (?P<quiz_num>\d+)\s*\n'
    r'^\s*Type: (?P<quiz_type>.+?)\s*\n'
    r'^\s*Format: (?P<format>.+?)\s*\n'
    r'^\s*Question: (?P<question>.+?)\s*\n'
    r'^\s*Pronunciation or Voca: (?P<pronunciation_or_voca>.+?)\s*\n'
    r'^\s*Options: (?P<options>.+?)\s*\n'
    r'^\s*Answer: (?P<answer>.+?)(?=\n\s*## \d|\Z)',
    re.MULTILINE | re.DOTALL
  )

  parsedQuizzes = []
  for match in pattern.finditer(data):
    quiz = match.groupdict()

    # 발음 및 단어
    if quiz['pronunciation_or_voca'] == 'None' or quiz['pronunciation_or_voca'] == None:
      quiz['pronunciation_or_voca'] = None
    # 객관식 번호
    if quiz['options'] == 'None' or quiz['options'] == None:
      quiz['options'] = None
    else:
      quiz['options'] = parseOption(quiz['options'])
    # 답
    if quiz['answer'] == "None" or quiz['answer'] == "None\n" or quiz['answer'] == None:
      quiz['answer'] = None
    else :
      quiz['answer'] = quiz['answer'].strip()

    parsedQuizzes.append(quiz)

  quizzes = [quiz_schema.Quiz(**quiz) for quiz in parsedQuizzes]
  return quiz_schema.QuizList(quizzes=quizzes)