from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hi!\nWelcome to Refy Trade Bot 🚀\n\nYou will receive updates here.\nThanks for choosing us!! 😊\n🚀 Activate Your Account & Start Earning!\n
To unlock your earning potential and start your journey with RefyTrade, place your first order now.\n
🛒 Order Value: ₹100\n
✅ Status: Instant Activation\n
👇  to pay:\n
please message our supporter : @RefyTrade"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
