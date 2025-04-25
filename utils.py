import os

def load_prompt_context():
    docs_path = "docs"
    result = ""
    for filename in os.listdir(docs_path):
        if filename.endswith(".txt"):
            with open(os.path.join(docs_path, filename), "r", encoding="utf-8") as f:
                result += f"\n[{filename.replace('.txt','').upper()}]\n" + f.read() + "\n"
    return result

def get_language_greeting(lang):
    if lang == "ru":
        return "👋 Добро пожаловать!\n\nЯ — 🤖 *AI ассистент отдела продаж* компании **AVALON** ..."
    elif lang == "uk":
        return "👋 Вітаю!\n\nЯ — 🤖 *AI-асистент відділу продажів* компанії **AVALON** ..."
    else:
        return "👋 Hello and welcome!\n\nI'm the 🤖 *AI sales assistant* at **AVALON** ..."
