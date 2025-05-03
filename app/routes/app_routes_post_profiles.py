"""
Routes pour la gestion des profils de post et la génération de contenu selon ces profils.
"""
from fastapi import APIRouter, Depends, Header, HTTPException, Body
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from app.prompts.prompts_post import create_post_type_schema
from app.agents.content_creator.content_creator import ContentCreator
from app.utils.get_brief_entreprise import load_brief
import os
from dotenv import load_dotenv

router = APIRouter(
    prefix="/post-profiles",
    tags=["Post Profiles"]
)

# Modèles Pydantic pour la validation des entrées
class PostProfileCreate(BaseModel):
    """Modèle pour la création d'un profil de post"""
    post_type: str = Field(..., description="Nom du type de post")
    audience: str = Field(..., description="Public cible du post")
    goal: List[str] = Field(..., description="Objectifs du post")
    format: Optional[str] = Field("libre", description="Format de contenu souhaité")
    tone: List[str] = Field(default=["Humain et accessible"], description="Ton à adopter")
    language_style: str = Field("neutre", description="Style de langage")
    emojis: str = Field("auto", description="Utilisation des emojis")
    structure: str = Field("libre", description="Structure du post")
    length: str = Field("moyen", description="Longueur cible du post")
    include_cta: bool = Field(False, description="Inclure un appel à l'action")

class GeneratePostRequest(BaseModel):
    """Modèle pour la génération d'un post à partir d'un profil"""
    brief_id: str = Field(..., description="ID du brief d'entreprise")
    idea: str = Field(..., description="Idée de contenu")
    profile: Dict[str, Any] = Field(..., description="Profil de post")

# Middleware d'authentification (à améliorer avec JWT)
API_KEY = os.getenv("API_KEY", "TA_CLE_SECRETE_ICI")  # À améliorer avec une variable d'environnement

async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Unauthorized")

# Endpoints
@router.get("/schema")
async def get_profile_schema():
    """Retourne le schéma JSON pour la création d'un profil de post"""
    return create_post_type_schema()

@router.post("/generate", dependencies=[Depends(verify_api_key)])
async def generate_post_from_profile(request: GeneratePostRequest):
    """
    Génère un post LinkedIn à partir d'un profil personnalisé
    """
    try:
        # Récupération du brief
        brief = load_brief(request.brief_id)
        if not brief:
            raise HTTPException(status_code=404, detail="Brief not found")
        
        # Instanciation du créateur de contenu
        content_creator = ContentCreator()
        
        # Génération du post
        post_content = content_creator.generate_post_from_profile(
            brief=brief,
            idea=request.idea,
            profile=request.profile
        )
        
        return {
            "content": post_content,
            "profile_used": request.profile
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
