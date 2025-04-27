# idea_generator.py

from openai import OpenAI
from app.prompts.prompts_ideas import get_idea_prompt
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL_BASE = os.getenv("MODEL_BASE")

class IdeaGenerator:
    def __init__(self, model=MODEL_BASE):
        self.model = model

    def generate_ideas(self, brief_entreprise: str) -> list:
        prompt = get_idea_prompt(brief_entreprise)
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=600
        )
        content = response.choices[0].message.content.strip()
        return self._parse_ideas(content)

    def _parse_ideas(self, text: str) -> list:
        import re
        lines = re.findall(r"\d+\.\s+(.*)", text)
        return lines