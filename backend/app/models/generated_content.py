# backend/app/models/generated_content.py
from pydantic import BaseModel

class GeneratedContent(BaseModel):
    script: str
    storyboard: list  # List of image URLs or storyboard descriptions
    video_url: str    # URL for generated video/animation
