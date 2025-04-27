# reviewer.py

from openai import OpenAI
from prompts_reviewer import get_review_prompt
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL_BASE = os.getenv("MODEL_BASE")

class Reviewer:
    def __init__(self, model=MODEL_BASE, criteria=None):
        self.model = model
        self.criteria = criteria or """
1. Clarté du message
2. Pertinence pour la cible LinkedIn
3. Ton professionnel et humain
4. Structure du post (accroche, développement, call-to-action)
5. Qualité d’écriture (orthographe, fluidité, lisibilité)
"""

    def review_post(self, post: str) -> dict:
        prompt = get_review_prompt(post, self.criteria)
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=800
        )
        content = response.choices[0].message.content.strip()
        
        # Extraction naïve de la note
        note = self.extract_score(content)
        return {
            "feedback": content,
            "score": note
        }

    def extract_score(self, content: str) -> float:
        import re
        match = re.search(r"Note globale\s*:\s*([0-9.]+)", content)
        if match:
            return float(match.group(1))
        return 0.0