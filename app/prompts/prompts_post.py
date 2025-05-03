"""
Module responsable de la génération des prompts pour les posts LinkedIn selon les profils définis.
"""
from typing import Dict, List, Any, Optional


def get_post_prompt_from_profile(profile: Dict[str, Any], brief: str, idea: str) -> str:
    """
    Génère un prompt complet pour créer un post LinkedIn basé sur un profil,
    un brief d'entreprise et une idée de contenu.
    
    Args:
        profile: Dictionnaire contenant les paramètres du type de post
        brief: Brief de l'entreprise (contexte, valeurs, etc.)
        idea: Idée spécifique pour ce post
        
    Returns:
        Le prompt complet prêt à être envoyé à l'API d'OpenAI
    """
    # Extraction des infos du profil (avec valeurs par défaut si manquantes)
    post_type     = profile.get("post_type", "Post LinkedIn")
    audience      = profile.get("audience", "public professionnel")
    goal          = ", ".join(profile.get("goal", []))
    format_       = profile.get("format", "libre")
    tone          = ", ".join(profile.get("tone", []))
    lang_style    = profile.get("language_style", "neutre")
    emojis        = profile.get("emojis", "auto")
    structure     = profile.get("structure", "libre")
    length        = profile.get("length", "moyen")
    include_cta   = profile.get("include_cta", False)

    # Interprétation de la longueur
    length_map = {
        "court": "< 500 caractères",
        "moyen": "entre 500 et 1000 caractères",
        "long": "entre 1000 et 1500 caractères",
    }
    length_desc = length_map.get(length, "jusqu'à 1500 caractères")

    # CTA éventuel
    cta_instruction = "- Termine le post avec une question ou un appel à commenter.\n" if include_cta else ""

    # Emojis
    emoji_instruction = {
        "oui": "- Utilise des emojis avec parcimonie si pertinent.",
        "non": "- N'utilise pas d'emojis.",
        "auto": "- Utilise des emojis si cela améliore l'engagement.",
    }.get(emojis, "")

    # Prompt final
    prompt = f"""
Tu es un expert en marketing LinkedIn.

Rédige un post à partir du brief et de l'idée suivante :

🔹 BRIEF :
{brief}

💡 IDÉE :
{idea}

👥 Audience cible : {audience}
🎯 Objectif : {goal}
📄 Format souhaité : {format_}
🎙️ Ton : {tone}
💬 Style de langue : {lang_style}
🏗️ Structure : {structure}
📏 Longueur cible : {length_desc}


Contraintes :
- Sois humain, pertinent et engageant.
{emoji_instruction}
- Le texte doit être pensé pour LinkedIn, pas Instagram.
{cta_instruction}
- Génère uniquement le texte du post, sans introduction ni explication.

Génère le post maintenant.
""".strip()

    return prompt


def create_post_type_schema() -> Dict[str, Any]:
    """
    Retourne le schéma JSON pour valider un type de post LinkedIn.
    Utile pour la documentation API et la validation côté frontend.
    
    Returns:
        Un schéma JSON décrivant la structure d'un type de post
    """
    return {
        "type": "object",
        "properties": {
            "post_type": {
                "type": "string",
                "description": "Nom du type de post (ex: 'Post storytelling', 'Annonce produit')",
                "default": "Post LinkedIn"
            },
            "audience": {
                "type": "string",
                "description": "Public cible du post",
                "default": "public professionnel"
            },
            "goal": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Objectifs du post (plusieurs possibles)",
                "default": ["Gagner en visibilité"]
            },
            "format": {
                "type": "string",
                "description": "Format de contenu souhaité",
                "enum": ["Histoire personnelle", "Mini-guide / tuto", "Opinion", "Résumé de lecture", "Étude de cas", "Thread", "libre"],
                "default": "libre"
            },
            "tone": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Ton à adopter (plusieurs possibles)",
                "default": ["Humain et accessible"]
            },
            "language_style": {
                "type": "string",
                "description": "Style de langage à utiliser",
                "enum": ["Tutoiement", "Vouvoiement", "Neutre"],
                "default": "neutre"
            },
            "emojis": {
                "type": "string",
                "description": "Utilisation des emojis",
                "enum": ["oui", "non", "auto"],
                "default": "auto"
            },
            "structure": {
                "type": "string",
                "description": "Structure du post",
                "enum": ["Hook + Développement + Conclusion", "Problème → Solution → Résultat", "libre"],
                "default": "libre"
            },
            "length": {
                "type": "string",
                "description": "Longueur cible du post",
                "enum": ["court", "moyen", "long"],
                "default": "moyen"
            },
            "include_cta": {
                "type": "boolean",
                "description": "Inclure un appel à l'action à la fin",
                "default": False
            }
        },
        "required": ["post_type", "audience", "goal"]
    }


# # from feedback_utils import get_feedback_insights

# def get_post_prompt_from_profile(profile: dict, brief: str, idea: str) -> str:
#     # Feedback stylistiques (appris via l'utilisateur)
#     # feedbacks = get_feedback_insights()
#     # preferences = "\n".join(f"- {f}" for f in feedbacks if f)
#     # if not preferences:
#     #     preferences = "- Aucune préférence définie"

#     # Extraction des infos du profil (avec valeurs par défaut si manquantes)
#     post_type     = profile.get("post_type", "Post LinkedIn")
#     audience      = profile.get("audience", "public professionnel")
#     goal          = ", ".join(profile.get("goal", []))
#     format_       = profile.get("format", "libre")
#     tone          = ", ".join(profile.get("tone", []))
#     lang_style    = profile.get("language_style", "neutre")
#     emojis        = profile.get("emojis", "auto")
#     structure     = profile.get("structure", "libre")
#     length        = profile.get("length", "moyen")
#     include_cta   = profile.get("include_cta", False)

#     # Interprétation de la longueur
#     length_map = {
#         "court": "< 500 caractères",
#         "moyen": "entre 500 et 1000 caractères",
#         "long": "entre 1000 et 1500 caractères",
#     }
#     length_desc = length_map.get(length, "jusqu’à 1500 caractères")

#     # CTA éventuel
#     cta_instruction = "- Termine le post avec une question ou un appel à commenter.\n" if include_cta else ""

#     # Emojis
#     emoji_instruction = {
#         "oui": "- Utilise des emojis avec parcimonie si pertinent.",
#         "non": "- N’utilise pas d’emojis.",
#         "auto": "- Utilise des emojis si cela améliore l’engagement.",
#     }.get(emojis, "")

#     # Prompt final
#     prompt = f"""
# Tu es un expert en marketing LinkedIn.

# Rédige un post à partir du brief et de l’idée suivante :

# 🔹 BRIEF :
# {brief}

# 💡 IDÉE :
# {idea}

# 👥 Audience cible : {audience}
# 🎯 Objectif : {goal}
# 📄 Format souhaité : {format_}
# 🎙️ Ton : {tone}
# 💬 Style de langue : {lang_style}
# 🏗️ Structure : {structure}
# 📏 Longueur cible : {length_desc}


# Contraintes :
# - Sois humain, pertinent et engageant.
# {emoji_instruction}
# - Le texte doit être pensé pour LinkedIn, pas Instagram.
# {cta_instruction}
# - Génère uniquement le texte du post, sans introduction ni explication.

# Génère le post maintenant.
# """.strip()

#     return prompt

# # 🧠 Préférences stylistiques apprises :
# # {preferences}

# # Exemple d'utilisation
# if __name__ == "__main__":
#     prompt = get_post_prompt_from_profile(
#         profile={
#             "post_type": "Annonce produit",
#             "audience": "Fondateurs de startups",
#             "goal": ["Gagner en visibilité", "Générer des leads"],
#             "format": "Mini-guide",
#             "tone": ["Expert", "Accessible"],
#             "language_style": "Vouvoiement",
#             "emojis": "oui",
#             "structure": "Problème → Solution → Résultat",
#             "length": "long",
#             "include_cta": True
#         },
#         brief="Nous lançons une nouvelle fonctionnalité qui permet aux utilisateurs de programmer leurs posts multi-réseaux.",
#         idea="Montrer comment cette feature fait gagner 2h par semaine"
#     )
#     print(prompt)