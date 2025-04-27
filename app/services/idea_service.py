# from app.services.prompts_ideas import PROMPTS_IDEAS  # si nécessaire
from app.agents.content_creator.idea_generator import IdeaGenerator  # Ton vrai générateur d'idée

def generate_idea(payload: dict):

    idea_generator = IdeaGenerator()

    brief_entreprise = payload.get("brief_entreprise", "Entreprise de cosmetique")
    brief_action = payload.get("brief_action", "Contenu général")

    try:
        idea = idea_generator.generate_ideas(brief_entreprise, brief_action)
        return {"idea": idea}
    except Exception as e:
        return {"error": str(e)}

def create_content(payload: dict):
    idea = payload.get("idea", "Pas d'idée fournie")
    try:
        content = f"Contenu complet basé sur l'idée : {idea}"  # Pour l'instant, on améliore après
        return {"content": content}
    except Exception as e:
        return {"error": str(e)}