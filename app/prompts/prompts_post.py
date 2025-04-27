# prompts.py
from feedback_utils import get_feedback_insights

def get_post_prompt(brief: str, demande: str) -> str:
        feedbacks = get_feedback_insights()
        
        preferences = "\n".join(f"- {f}" for f in feedbacks if f)
        if not preferences:
            preferences = "- Aucune préférence définie"

        prompt = f"""
Tu es un expert en marketing LinkedIn. Rédige un post à partir du brief suivant :

BRIEF :
{brief}

DEMANDE :
{demande}

Préférences stylistiques apprises :
{preferences}

Contraintes :
- Sois humain et engageant
- Utilise des emojis si pertinent
- Ne dépasse pas 1500 caractères
- Tu écris pour LinkedIn, pas Instagram

Génère uniquement le texte du post sans introduction ni explication.
"""
