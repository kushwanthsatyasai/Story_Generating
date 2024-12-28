# backend/app/services/ai_service.py
import openai  # Ensure you have OpenAI's Python package installed

def call_gpt_for_script(story_input):
    """
    Generate a detailed script using GPT.
    """
    prompt = (
        f"Generate a detailed script for a {story_input.genre} story titled '{story_input.title}'. "
        f"The story description is: {story_input.description}. The key characters are: {story_input.character_details}. "
        f"Output the script in a structured format with scene headings, actions, and dialogues."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Replace with the desired OpenAI model
            messages=[{"role": "system", "content": "You are a scriptwriter."}, {"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=3000
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error in GPT script generation: {e}")
        return "An error occurred while generating the script."
