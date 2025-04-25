
import os
import telegram
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from fastapi import FastAPI, Request

from handlers import start_handler, message_handler

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Создаём Telegram Application
application = Application.builder().token(TELEGRAM_TOKEN).build()
application.add_handler(CommandHandler("start", start_handler))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

# Создаём FastAPI приложение
fastapi_app = FastAPI()
bot = telegram.Bot(token=TELEGRAM_TOKEN)

@fastapi_app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = telegram.Update.de_json(data, bot)
    await application.process_update(update)
    return {"ok": True}
