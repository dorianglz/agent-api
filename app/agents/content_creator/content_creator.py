# content_creator.py

from openai import OpenAI
from prompts import get_post_prompt
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL_BASE = os.getenv("MODEL_BASE")

class ContentCreator:
    def __init__(self, model=MODEL_BASE):
        self.model = model

    def generate_post(self, brief: str, demande: str) -> str:
        prompt = get_post_prompt(brief, demande)
        print(prompt)
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()

    def revise_post(self, original_post: str, feedback: str) -> str:
        prompt = f"""
Voici un post LinkedIn à améliorer :

POST ORIGINAL :
{original_post}

Voici un feedback d’un expert :
{feedback}

Réécris un nouveau post en corrigeant les problèmes signalés. Conserve le sujet, améliore la clarté, la structure et le ton.
"""
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()