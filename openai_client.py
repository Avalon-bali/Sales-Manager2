import os
import openai

def ask_openai(user_input: str) -> str:
    # Загрузка актуального system_prompt
    with open("system_prompt.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()

    # Загрузка контекста из docs/*.txt
    context = ""
    docs_path = "docs"
    for filename in os.listdir(docs_path):
        if filename.endswith(".txt"):
            with open(os.path.join(docs_path, filename), "r", encoding="utf-8") as doc:
                context += f"\n[{filename.replace('.txt', '').upper()}]\n" + doc.read()

    messages = [
        {"role": "system", "content": system_prompt + "\n" + context},
        {"role": "user", "content": user_input}
    ]

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    return response.choices[0].message.content.strip()
