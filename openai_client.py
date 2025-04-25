import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_openai(user_input: str) -> str:
    # Загружаем system_prompt
    with open("system_prompt.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()

    # Загружаем контекст из docs
    context = ""
    docs_path = "docs"
    for filename in os.listdir(docs_path):
        if filename.endswith(".txt"):
            with open(os.path.join(docs_path, filename), "r", encoding="utf-8") as file:
                content = file.read()
                context += f"\n[{filename.replace('.txt', '').upper()}]\n{content}"

    # Отправляем в GPT
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt + "\n" + context},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content.strip()
