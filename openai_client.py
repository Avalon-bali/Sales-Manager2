import os
import openai
import random

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

def off_topic_reply() -> str:
    responses = [
        "Хороший вопрос, но я специализируюсь только на проектах Avalon и инвестициях на Бали 😊",
        "Это немного вне моей компетенции. Зато я могу рассказать всё про OM, BUDDHA и TAO — наши топовые объекты 🏝",
        "Давайте вернёмся к теме недвижимости на Бали 🙌 Я с радостью подскажу по Avalon!",
        "Я помогу вам с инвестициями и апартаментами на Бали, но на другие темы, к сожалению, не отвечаю.",
        "Похоже, это не совсем по моей части 🤔 Моя задача — консультировать по недвижимости Avalon на Бали!",
        "Я могу быть полезен, если вас интересуют апартаменты, ROI или переезд на Бали с Avalon.",
        "Давайте сосредоточимся на недвижимости 😊 Например, вы уже смотрели наш проект TAO в Переренане?",
    ]
    return random.choice(responses)

def ask_openai(user_input: str) -> str:
    if not is_on_topic(user_input):
        return off_topic_reply()

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
