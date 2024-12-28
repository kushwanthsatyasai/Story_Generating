import os
import openai

def generate_storyboard(prompt: str) -> str:
    # Generate scenes description
    scenes = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Describe storyboard scenes for: {prompt}"}],
    )["choices"][0]["message"]["content"].split("\n")

    storyboard_dir = "public/storyboards/"
    os.makedirs(storyboard_dir, exist_ok=True)

    storyboard_paths = []
    for idx, scene in enumerate(scenes):
        response = openai.Image.create(
            prompt=scene,
            n=1,
            size="512x512"
        )
        image_path = os.path.join(storyboard_dir, f"scene_{idx}.png")
        os.system(f"wget {response['data'][0]['url']} -O {image_path}")
        storyboard_paths.append(image_path)

    return storyboard_dir
