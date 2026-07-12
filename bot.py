import os
import sys
import logging
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load token dari Environment Variable (BUKAN dari file .env untuk production)
load_dotenv()
TOKEN = os.getenv("8940266091:AAHfUeHEGaZMiYwkGfCUacIX3JODRxK5yPA")

if not TOKEN:
    logger.error("❌ TOKEN TIDAK DITEMUKAN! Cek environment variable di dashboard.")
    sys.exit(1)

# Handler Start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        welcome_text = "👋 Halo! Klik tombol di bawah untuk claim airdrop."
        keyboard = [["🎁 Claim Airdrop"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text(welcome_text, reply_markup=reply_markup)
    except Exception as e:
        logger.error(f"Error di start: {e}")

# Handler Tombol Claim
async def handle_claim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # GANTI link ini dengan website asli Anda
        link = "https://example.com/claim-airdrop" 
        response = f"🎉 *Claim Airdrop*\n\nKlik link berikut:\n[🔗 Klik di sini]({link})"
        await update.message.reply_text(response, parse_mode="Markdown")
    except Exception as e:
        logger.error(f"Error di claim: {e}")

# Main
def main():
    logger.info("🚀 Bot mulai berjalan...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_claim))
    logger.info("✅ Bot siap menerima pesan!")
    app.run_polling()

if __name__ == "__main__":
    main()
