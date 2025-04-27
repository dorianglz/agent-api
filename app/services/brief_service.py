import openai
from dotenv import load_dotenv
import os

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL_BASE = os.getenv("MODEL_BASE")

def call_openai_for_brief(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_BASE,
        messages=[
            {"role": "system", "content": "Tu es un expert en stratégie marketing et branding."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=1500
    )
    return response.choices[0].message.content