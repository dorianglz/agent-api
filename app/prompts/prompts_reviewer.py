# prompts_reviewer.py

def get_review_prompt(post: str, criteria: str) -> str:
    return f"""
Tu es un expert en personal branding sur LinkedIn. Voici un post à évaluer :

POST :
{post}

Tu dois analyser ce post selon les critères suivants :
{criteria}

Pour chaque critère, donne un feedback court (une phrase) + une note sur 10.

Ensuite, donne une **note globale entre 0.0 et 1.0**, et justifie-la.

Réponds dans le format suivant :
- Feedbacks : ...
- Note globale : ...
"""