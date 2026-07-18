from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

TOKEN = "BURAYA_BOT_TOKENİNİ_YAZ"

signals = [
    "🟢 BTC/USDT\nYön: LONG\nGiriş: 118500\nTP: 120000\nSL: 117500",
    "🟢 ETH/USDT\nYön: LONG\nGiriş: 4200\nTP: 4300\nSL: 4150",
    "🔴 SOL/USDT\nYön: SHORT\nGiriş: 210\nTP: 200\nSL: 215"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Alpha Coin Signal Bot'a hoş geldin!\n\n/signal yazarak sinyal al."
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(signals))

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

print("Bot çalışıyor...")
app.run_polling()
