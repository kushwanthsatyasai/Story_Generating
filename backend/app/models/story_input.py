# backend/app/models/story_input.py
from pydantic import BaseModel

class StoryInput(BaseModel):
    title: str
    description: str
    genre: str
    character_details: dict
    desired_output_format: str  # e.g., video, storyboard, etc.
