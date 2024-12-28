from fastapi import APIRouter, HTTPException
from app.services.storyboard_service import generate_storyboard

router = APIRouter()

@router.post("/generate-storyboard")
async def generate_storyboard_endpoint(prompt: str):
    try:
        storyboard_path = generate_storyboard(prompt)
        return {"storyboard_path": storyboard_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
