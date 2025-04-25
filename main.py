import os
import telegram
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from fastapi import FastAPI, Request

from handlers import start_handler, message_handler

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Создание FastAPI и Telegram компонентов
application = Application.builder().token(TELEGRAM_TOKEN).build()
bot = telegram.Bot(token=TELEGRAM_TOKEN)
fastapi_app = FastAPI()

# Подключение обработчиков
application.add_handler(CommandHandler("start", start_handler))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

# Флаг инициализации
app_initialized = False

@fastapi_app.post("/webhook")
async def webhook(request: Request):
    global app_initialized
    if not app_initialized:
        await application.initialize()
        app_initialized = True

    data = await request.json()
    update = telegram.Update.de_json(data, bot)
    await application.process_update(update)
    return {"ok": True}
