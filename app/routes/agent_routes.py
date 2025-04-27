from fastapi import APIRouter, Depends, Header, HTTPException
from app.services.idea_service import generate_idea, create_content
from app.prompts.prompts_brief_creator import get_brief_generation_prompt
from app.services.brief_service import call_openai_for_brief

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

@router.post("/generate-brief")
async def generate_brief(payload: dict):
    try:
        prompt = get_brief_generation_prompt(payload)
        brief_result = call_openai_for_brief(prompt)
        return {"brief": brief_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))