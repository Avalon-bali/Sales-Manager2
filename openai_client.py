import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# Ключевые слова по теме Avalon
ALLOWED_KEYWORDS = [
    "avalon", "om", "buddha", "tao", "инвестиции", "апартаменты", "бали",
    "ROI", "недвижимость", "перенос строительства", "лизхолд", "реновация", "управляющая компания",
    "продажа", "доход", "проект", "berawa", "pererenan", "canggu", "om apartments", "buddha club house"
]

def is_on_topic(text: str) -> bool:
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in ALLOWED_KEYWORDS)

def ask_openai(user_input: str) -> str:
    if not is_on_topic(user_input):
        return "Извините, я могу помочь только по вопросам, связанным с проектами Avalon и инвестициями на Бали."

    with open("system_prompt.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()

    context = ""
    docs_path = "docs"
    for filename in os.listdir(docs_path):
        if filename.endswith(".txt"):
            with open(os.path.join(docs_path, filename), "r", encoding="utf-8") as file:
                content = file.read()
                context += f"\n[{filename.replace('.txt', '').upper()}]\n{content}"

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt + "\n" + context},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content.strip()
