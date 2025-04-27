# prompts_ideas.py

def get_idea_prompt(brief_entreprise: str) -> str:
    return f"""
Tu es un créatif LinkedIn expérimenté.

Contexte entreprise :
{brief_entreprise}

Génère 5 idées de posts LinkedIn, chacun avec un style différent :
- Un inspirant
- Un éducatif
- Un storytelling
- Un factuel/chiffré
- Un conversationnel

Chaque idée doit être concise (1-2 lignes), impactante et orientée vers le business.

Format :

1. Inspirant : ...
2. Educatif : ...
3. Storytelling : ...
4. Factuel : ...
5. Conversationnel : ...
"""