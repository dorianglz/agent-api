# prompts_ideas.py

def get_idea_prompt(brief_entreprise: str, brief_action: str) -> str:
    return f"""
Tu es un expert en stratégie de contenu sur LinkedIn.

Voici un brief d'entreprise :
{brief_entreprise}

Et un objectif d'action :
{brief_action}

Propose 5 idées de posts LinkedIn concrets, orientés business, engageants et réalistes. Chaque idée doit être :
- concise (1-2 lignes)
- originale
- alignée avec l’objectif

Réponds au format :
1. ...
2. ...
3. ...
"""