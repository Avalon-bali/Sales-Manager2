import os
import openai
from utils import load_prompt_context

openai.api_key = os.getenv("OPENAI_API_KEY")

docs_context = load_prompt_context()

def ask_openai(user_input: str) -> str:
    system_prompt = open("system_prompt.txt", "r", encoding="utf-8").read()
    messages = [
        {"role": "system", "content": system_prompt + docs_context},
        {"role": "user", "content": user_input}
    ]
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    return response.choices[0].message.content.strip()
