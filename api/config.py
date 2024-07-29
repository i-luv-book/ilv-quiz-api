import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    STABLE_DIFFUSION_API_KEY: str = os.getenv("STABLE_DIFFUSION_API_KEY")
    OPENAI_QUIZ_MODEL: str = os.getenv("QUIZ_MODEL")
    OPENAI_WORD_MODEL: str = os.getenv("WORD_MODEL")
    
settings = Settings()