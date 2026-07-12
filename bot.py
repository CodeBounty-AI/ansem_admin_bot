import os
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ===================== KONFIGURASI =====================
load_dotenv()

TOKEN = os.getenv("8940266091:AAHfUeHEGaZMiYwkGfCUacIX3JODRxK5yPA")
if not TOKEN:
    raise ValueError("Token tidak ditemukan! Pastikan file .env berisi TELEGRAM_BOT_TOKEN.")

# ===================== HANDLER PERINTAH =====================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Kirim pesan sambutan dan tombol Claim Airdrop."""
    welcome_text = (
        "👋 Halo! Selamat datang di Bot Airdrop.\n"
        "Klik tombol di bawah untuk melakukan claim."
    )

    # Hanya satu tombol
    keyboard = [["🎁 Claim Airdrop"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# ===================== HANDLER TOMBOL =====================

async def handle_claim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Kirim link website saat tombol Claim ditekan."""
    # Ganti link berikut dengan URL website Anda
    link = "https://example.com/claim-airdrop"
    response = (
        f"🎉 *Claim Airdrop*\n\n"
        f"Klik link di bawah ini untuk melakukan claim:\n"
        f"[🔗 Klik di sini]({link})\n\n"
        "Pastikan Anda sudah menghubungkan wallet yang terdaftar."
    )
    await update.message.reply_text(response, parse_mode="Markdown", disable_web_page_preview=False)

# ===================== MAIN =====================

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Handler untuk /start
    app.add_handler(CommandHandler("start", start))

    # Handler untuk semua pesan teks (hanya tombol "🎁 Claim Airdrop" yang akan diproses)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_claim))

    print("🤖 Bot sedang berjalan dengan menu sederhana...")
    app.run_polling()

if __name__ == "__main__":
    main()
