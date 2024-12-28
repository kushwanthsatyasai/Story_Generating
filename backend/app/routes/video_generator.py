from fastapi import APIRouter, HTTPException
from app.services.video_service import generate_video

router = APIRouter()

@router.post("/generate-video")
async def generate_video_endpoint(prompt: str):
    try:
        video_path = generate_video(prompt)
        return {"video_path": video_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
