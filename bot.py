import os
import sys
import logging
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info("🚀 BOT SEDANG DIJALANKAN (VERSI DEBUG)...")

# 1. CEK ENVIRONMENT VARIABLE
logger.info("📋 Mencoba membaca environment variable...")
load_dotenv()
token = os.getenv("TELEGRAM_BOT_TOKEN")

if not token:
    logger.error("❌ TOKEN TIDAK DITEMUKAN!")
    logger.info("📋 Daftar semua environment variable yang tersedia:")
    for key in os.environ.keys():
        logger.info(f"   - {key}")
    sys.exit(1)
else:
    # Aman: hanya tampilkan 4 karakter pertama agar tidak bocor
    logger.info(f"✅ Token ditemukan! (4 karakter pertama: {token[:4]}...)")

# 2. HANDLER
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["🎁 Claim Airdrop"]]
    await update.message.reply_text(
        "👋 Halo! Klik tombol di bawah.", 
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

async def claim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎉 Claim Airdrop: https://example.com")

# 3. MAIN
def main():
    logger.info("🚀 Membangun aplikasi bot...")
    try:
        app = ApplicationBuilder().token(token).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, claim))
        
        logger.info("✅ Bot siap. Menjalankan polling...")
        app.run_polling()
    except Exception as e:
        logger.error(f"🚨 BOT CRASH! Error: {e}")
        if "Conflict" in str(e):
            logger.error("⚠️ KONFLIK: Ada bot lain yang berjalan dengan token ini.")
            logger.error("💡 Solusi: Revoke token di BotFather dan buat token baru.")
        sys.exit(1)

if __name__ == "__main__":
    main()
