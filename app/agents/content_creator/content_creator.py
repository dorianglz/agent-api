"""
Agent principal pour la création de contenu LinkedIn.
"""
from openai import OpenAI
from app.prompts.prompts_post import get_post_prompt_from_profile
# from app.prompts.prompts_post import get_post_prompt
from dotenv import load_dotenv
import os
from typing import Dict, Any, Optional

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL_BASE = os.getenv("MODEL_BASE")

class ContentCreator:
    """
    Agent responsable de générer du contenu LinkedIn à partir de briefs et d'idées.
    """
    def __init__(self, model=MODEL_BASE):
        self.model = model

    def generate_post(self, brief: str, demande: str) -> str:
        """
        Génère un post LinkedIn en utilisant le prompt standard
        
        Args:
            brief: Brief d'entreprise
            demande: Demande spécifique pour ce post
            
        Returns:
            Le contenu du post généré
        """
        prompt = get_post_prompt(brief, demande)
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    
    def generate_post_from_profile(self, brief: str, idea: str, profile: Dict[str, Any]) -> str:
        """
        Génère un post LinkedIn à partir d'un profil de post personnalisé
        
        Args:
            brief: Brief d'entreprise
            idea: Idée de contenu
            profile: Profil de post avec les préférences de style
            
        Returns:
            Le contenu du post généré
        """
        prompt = get_post_prompt_from_profile(profile, brief, idea)
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()

    def revise_post(self, original_post: str, feedback: str) -> str:
        """
        Révise un post LinkedIn en fonction du feedback reçu
        
        Args:
            original_post: Contenu original du post
            feedback: Feedback sur le post à améliorer
            
        Returns:
            La version révisée du post
        """
        prompt = f"""
Voici un post LinkedIn à améliorer :

POST ORIGINAL :
{original_post}

Voici un feedback d'un expert :
{feedback}

Réécris un nouveau post en corrigeant les problèmes signalés. Conserve le sujet, améliore la clarté, la structure et le ton.
"""
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()

# # content_creator.py

# from openai import OpenAI
# from prompts import get_post_prompt
# from dotenv import load_dotenv
# import os

# load_dotenv()
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# MODEL_BASE = os.getenv("MODEL_BASE")

# class ContentCreator:
#     def __init__(self, model=MODEL_BASE):
#         self.model = model

#     def generate_post(self, brief: str, demande: str) -> str:
#         prompt = get_post_prompt(brief, demande)
#         print(prompt)
#         response = client.chat.completions.create(
#             model=self.model,
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.8,
#             max_tokens=500
#         )
#         return response.choices[0].message.content.strip()

#     def revise_post(self, original_post: str, feedback: str) -> str:
#         prompt = f"""
# Voici un post LinkedIn à améliorer :

# POST ORIGINAL :
# {original_post}

# Voici un feedback d’un expert :
# {feedback}

# Réécris un nouveau post en corrigeant les problèmes signalés. Conserve le sujet, améliore la clarté, la structure et le ton.
# """
#         response = client.chat.completions.create(
#             model=self.model,
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.7,
#             max_tokens=500
#         )
#         return response.choices[0].message.content.strip()