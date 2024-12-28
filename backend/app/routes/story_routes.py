from fastapi import APIRouter
from app.utils.database import save_story

router = APIRouter()

@router.post("/save-story")
async def save_generated_story(user_id: str, story: str):
    try:
        save_story(user_id, story)
        return {"message": "Story saved successfully!"}
    except Exception as e:
        return {"error": str(e)}
