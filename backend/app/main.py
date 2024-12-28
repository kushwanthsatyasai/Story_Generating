from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()

# Load OpenAI API Key
openai.api_key = "sk-...eKAA"

class StoryPrompt(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_story(prompt: StoryPrompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt.prompt,
            max_tokens=500,
        )
        return {"story": response.choices[0].text.strip()}
    except Exception as e:
        return {"error": str(e)}
