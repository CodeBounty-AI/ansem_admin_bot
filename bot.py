import os
import sys
import logging
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Konfigurasi logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Coba baca dari .env (untuk lokal), tapi utamakan environment variable sistem
load_dotenv()
TOKEN = os.getenv("8940266091:AAHfUeHEGaZMiYwkGfCUacIX3JODRxK5yPA")

if not TOKEN:
    logger.error("❌ TOKEN TIDAK DITEMUKAN! Pastikan environment variable 'TELEGRAM_BOT_TOKEN' sudah diset di dashboard.")
    sys.exit(1)  # Keluar dengan kode error, log akan terlihat

# Handler start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        welcome = "👋 Halo! Klik tombol di bawah untuk claim airdrop."
        keyboard = [["🎁 Claim Airdrop"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text(welcome, reply_markup=reply_markup)
    except Exception as e:
        logger.error(f"Error di start: {e}")

# Handler claim
async def handle_claim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        link = "https://example.com/claim-airdrop"  # Ganti dengan link asli
        resp = f"🎉 *Claim Airdrop*\n\nKlik link berikut:\n[🔗 Klik di sini]({link})"
        await update.message.reply_text(resp, parse_mode="Markdown")
    except Exception as e:
        logger.error(f"Error di claim: {e}")

def main():
    logger.info("🚀 Bot mulai berjalan...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_claim))
    logger.info("✅ Bot siap menerima pesan!")
    app.run_polling()

if __name__ == "__main__":
    main()
