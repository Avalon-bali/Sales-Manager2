from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from openai_client import ask_openai
from utils import get_language_greeting

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = update.effective_user.language_code
    greeting = get_language_greeting(lang)
    await update.message.reply_text(greeting, parse_mode=ParseMode.MARKDOWN)

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    response = ask_openai(user_input)
    await update.message.reply_text(response)
