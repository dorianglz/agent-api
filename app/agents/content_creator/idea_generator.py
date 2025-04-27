from openai import OpenAIError, OpenAI
import os
from dotenv import load_dotenv
from app.prompts.prompts_ideas import get_idea_prompt

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL_LIGHT = os.getenv("MODEL_LIGHT")

class IdeaGenerator:
    @staticmethod
    def generate_ideas(brief_entreprise: str) -> list:
        prompt = get_idea_prompt(brief_entreprise)

        for attempt in range(2):  # Autoriser 2 tentatives
            try:
                response = client.chat.completions.create(
                    model=MODEL_LIGHT,
                    messages=[
                        {"role": "system", "content": "Tu es un expert en stratégie de contenu pour LinkedIn."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=600,
                    timeout=30,  # Timeout propre
                )
                ideas_text = response.choices[0].message.content.strip()

                if not ideas_text:
                    raise ValueError("La réponse d'OpenAI est vide.")

                # Parse les idées retournées
                ideas = [line.strip()[3:] for line in ideas_text.splitlines() if line.strip() and line.strip()[0].isdigit()]
                if not ideas:
                    raise ValueError("Impossible d'extraire des idées valides.")

                return ideas

            except (OpenAIError, ValueError) as e:
                print(f"❗ Tentative {attempt+1} échouée : {e}")
                if attempt == 1:
                    raise Exception("Échec permanent après 2 tentatives pour générer des idées.")