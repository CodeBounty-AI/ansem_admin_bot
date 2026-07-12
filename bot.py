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
    logger.error("❌ TOKEN TIDAK DITEMUKAN!")
    exit(1)

logger.info("✅ Token berhasil dibaca.")

# ---------- HANDLER START (DENGAN LOG) ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        logger.info(f"📩 Menerima perintah /start dari user {update.effective_user.id}")
        
        # Pesan sambutan
        welcome_text = "👋 Halo! Selamat datang di Bot Airdrop.\nKlik tombol di bawah untuk claim."
        
        # Buat keyboard
        keyboard = [
            ["🎁 Claim Airdrop"]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
        
        # Kirim pesan + keyboard
        await update.message.reply_text(welcome_text, reply_markup=reply_markup)
        logger.info("✅ Pesan dan keyboard berhasil dikirim.")
        
    except Exception as e:
        logger.error(f"❌ Error di handler start: {e}")
        # Kirim pesan darurat tanpa keyboard agar user tahu ada masalah
        await update.message.reply_text("Maaf, terjadi kesalahan. Silakan coba lagi nanti.")

# ---------- HANDLER CLAIM ----------
async def handle_claim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        logger.info(f"📩 Tombol Claim ditekan oleh user {update.effective_user.id}")
        link = "https://example.com/claim-airdrop"  # Ganti dengan link Anda
        resp = f"🎉 *Claim Airdrop*\n\nKlik link berikut:\n[🔗 Klik di sini]({link})"
        await update.message.reply_text(resp, parse_mode="Markdown")
        logger.info("✅ Pesan claim berhasil dikirim.")
    except Exception as e:
        logger.error(f"❌ Error di handler claim: {e}")

# ---------- HANDLER UNKNOWN (FALLBACK) ----------
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Jika user mengetik sembarang selain tombol
    await update.message.reply_text(
        "Silakan gunakan tombol di bawah atau kirim /start untuk memulai ulang.",
        reply_markup=ReplyKeyboardMarkup([["🎁 Claim Airdrop"]], resize_keyboard=True)
    )

# ---------- MAIN ----------
def main():
    logger.info("🚀 Bot mulai berjalan...")
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Daftarkan handler
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Regex('^🎁 Claim Airdrop$'), handle_claim))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown))
    
    logger.info("✅ Bot siap menerima pesan! Menjalankan polling...")
    app.run_polling()

if __name__ == "__main__":
    main()
