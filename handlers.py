from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = update.effective_user.language_code

    if lang == "ru":
        greeting = (
            "👋 Добро пожаловать!\n\n"
            "Я — 🤖 *AI ассистент отдела продаж* компании **AVALON** — девелопера инвестиционной недвижимости на Бали.\n\n"
            "🏠 Вы можете задать мне любой вопрос о наших проектах (OM, BUDDHA, TAO), доходе от аренды, ROI, управлении недвижимостью или переезде на Бали.\n\n"
            "🧠 Я постараюсь максимально помочь — а при необходимости вас свяжет наш менеджер по продажам.\n\n"
            "🌐 Пишите на любом языке — я отвечу соответственно."
        )
    elif lang == "uk":
        greeting = (
            "👋 Вітаю!\n\n"
            "Я — 🤖 *AI-асистент відділу продажів* компанії **AVALON** — девелопера інвестиційної нерухомості на Балі.\n\n"
            "🏠 Ви можете поставити будь-яке запитання щодо проєктів (OM, BUDDHA, TAO), доходу, ROI, управління або переїзду.\n\n"
            "🧠 Я зроблю все можливе, щоб допомогти — а за потреби вас зв'яжуть з менеджером.\n\n"
            "🌐 Пишіть будь-якою мовою — я відповім відповідно."
        )
    else:
        greeting = (
            "👋 Hello and welcome!\n\n"
            "I'm the 🤖 *AI sales assistant* at **AVALON** — a real estate development company based in Bali.\n\n"
            "🏠 You can ask me anything about our investment projects (OM, BUDDHA, TAO), rental income, ROI, property management, or moving to Bali.\n\n"
            "🧠 I’ll do my best to help you — and if needed, one of our real sales managers will follow up personally.\n\n"
            "🌐 Feel free to write in *any language* — I’ll understand and reply accordingly."
        )

    await update.message.reply_text(greeting, parse_mode=ParseMode.MARKDOWN)
