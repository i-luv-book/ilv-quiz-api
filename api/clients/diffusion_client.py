import requests
from io import BytesIO

from ..config import settings
from api.clients.prompts.tale_prompt import talePromptGenerator

class DiffusionClient:
  # 동화 이미지 요청
  def requestImages(self):
    response = requests.post(
      f"https://api.stability.ai/v2beta/stable-image/generate/sd3",
      headers={
          "authorization": f"Bearer " + settings.STABLE_DIFFUSION_API_KEY,
          "accept": "image/*"
      },
      files={"none": ''},
      data={
          "prompt": talePromptGenerator.processTaleFirstImagePrompt(),
          "output_format": "jpeg",
          "model" : "sd3-large",
          "seed" : 200,
          "negative_prompt": "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime"
      },
    )

    return BytesIO(response.content)