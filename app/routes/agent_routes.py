from fastapi import APIRouter, Depends, Header, HTTPException
from app.services.idea_service import generate_idea, create_content

router = APIRouter(
    prefix="/agent",
    tags=["Agent Operations"]
)

API_KEY = "TA_CLE_SECRETE_ICI"  # à sécuriser

async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Unauthorized")

@router.post("/generate-idea", dependencies=[Depends(verify_api_key)])
async def generate_idea_endpoint(payload: dict):
    return generate_idea(payload)

@router.post("/create-content", dependencies=[Depends(verify_api_key)])
async def create_content_endpoint(payload: dict):
    return create_content(payload)