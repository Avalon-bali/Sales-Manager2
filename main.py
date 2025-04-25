import os
import telegram
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from fastapi import FastAPI, Request
import asyncio

from handlers import start_handler, message_handler

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Создаём FastAPI и Telegram компоненты
fastapi_app = FastAPI()
application = Application.builder().token(TELEGRAM_TOKEN).build()

# Добавляем обработчики
application.add_handler(CommandHandler("start", start_handler))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

# Флаг инициализации
app_ready = False

@fastapi_app.on_event("startup")
async def on_startup():
    global app_ready
    if not app_ready:
        await application.initialize()
        await application.bot.initialize()
        await application.start()
        app_ready = True

@fastapi_app.on_event("shutdown")
async def on_shutdown():
    await application.stop()
    await application.shutdown()

@fastapi_app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = telegram.Update.de_json(data, application.bot)
    await application.process_update(update)
    return {"ok": True}
