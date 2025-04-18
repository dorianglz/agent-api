def generate_idea(payload: dict):
    # Simule ton idée, ici on branchera ton idea_generator
    subject = payload.get("subject", "Contenu général")
    return {"idea": f"Idée originale pour : {subject}"}

def create_content(payload: dict):
    # Simule création de contenu, ici on branchera ton content_creator
    idea = payload.get("idea", "Pas d'idée fournie")
    return {"content": f"Contenu complet basé sur l'idée : {idea}"}