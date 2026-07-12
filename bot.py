import os
import sys
import logging
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

# ======== DEBUG: Cek variabel yang tersedia ========
print("🔍 [DEBUG] Mencoba membaca TOKEN...")
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if TOKEN:
    print(f"✅ [DEBUG] Token ditemukan! (5 karakter pertama: {TOKEN[:5]}...)")
else:
    print("❌ [DEBUG] Token TIDAK ditemukan!")
    print("📋 [DEBUG] Daftar semua environment variable yang tersedia:")
    for key in os.environ.keys():
        print(f"   - {key}")
    sys.exit(1)

# ======== KODE UTAMA ========
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        welcome = "👋 Halo! Klik tombol di bawah untuk claim airdrop."
        keyboard = [["🎁 Claim Airdrop"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text(welcome, reply_markup=reply_markup)
    except Exception as e:
        logger.error(f"Error di start: {e}")

async def handle_claim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        link = "https://example.com/claim-airdrop"  # Ganti dengan link Anda
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
