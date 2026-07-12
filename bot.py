import os
import logging
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ---------- LOGGING ----------
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ---------- BACA TOKEN ----------
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    logger.error("❌ TOKEN TIDAK DITEMUKAN! Pastikan environment variable TELEGRAM_BOT_TOKEN sudah diset.")
    exit(1)

logger.info("✅ Token berhasil dibaca.")

# ---------- HANDLER START ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        welcome = "👋 Halo! Selamat datang di Bot Airdrop.\nKlik tombol di bawah untuk claim."
        keyboard = [["🎁 Claim Airdrop"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text(welcome, reply_markup=reply_markup)
    except Exception as e:
        logger.error(f"Error di start: {e}")

# ---------- HANDLER CLAIM ----------
async def handle_claim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # GANTI link ini dengan website Anda
        link = "https://example.com/claim-airdrop"
        resp = f"🎉 *Claim Airdrop*\n\nKlik link berikut:\n[🔗 Klik di sini]({link})"
        await update.message.reply_text(resp, parse_mode="Markdown")
    except Exception as e:
        logger.error(f"Error di claim: {e}")

# ---------- MAIN ----------
def main():
    logger.info("🚀 Bot mulai berjalan...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_claim))
    
    try:
        logger.info("✅ Bot siap menerima pesan! Menjalankan polling...")
        app.run_polling()
    except Exception as e:
        logger.error(f"❌ Bot CRASH! Error: {e}")
        if "Conflict" in str(e):
            logger.error("⚠️ Terdeteksi KONFLIK! Ada bot lain yang berjalan dengan token yang sama.")
            logger.error("➡️  Solusi: Revoke token di BotFather dan buat token baru.")
        exit(1)

if __name__ == "__main__":
    main()
