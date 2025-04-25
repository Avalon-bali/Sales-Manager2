from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from handlers import start_handler, message_handler
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

# webhook-only: listen on /webhook
from fastapi import FastAPI, Request
import telegram

bot = telegram.Bot(token=TELEGRAM_TOKEN)
fastapi_app = FastAPI()

@app.on_startup
async def on_startup(app):
    webhook_url = os.getenv("WEBHOOK_URL", "https://sales-manager2.onrender.com/webhook")
    await bot.set_webhook(webhook_url)

@fastapi_app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()
    update = telegram.Update.de_json(data, bot)
    await app.update_queue.put(update)
    return {"ok": True}

if __name__ == "__main__":
    app.run_polling()
