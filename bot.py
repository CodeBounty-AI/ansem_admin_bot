import os
import sys
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

print("🚀 BOT MULAI...")

# 1. Baca token
print("📋 Mencoba membaca token...")
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    print("❌ TOKEN TIDAK DITEMUKAN!")
    print("Daftar semua environment variable:")
    for key in os.environ.keys():
        print(f"  {key}")
    sys.exit(1)

print(f"✅ Token ditemukan (4 karakter pertama: {TOKEN[:4]}...)")

# 2. Handler start
async def start(update: Update, context):
    print("📩 Handler start dipanggil")
    keyboard = [["🎁 Claim Airdrop"]]
    await update.message.reply_text(
        "👋 Halo! Klik tombol di bawah.",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

# 3. Handler claim
async def claim(update: Update, context):
    print("📩 Handler claim dipanggil")
    await update.message.reply_text("🎉 Claim: https://example.com")

# 4. Main
def main():
    print("🚀 Membangun aplikasi...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Regex('^🎁 Claim Airdrop$'), claim))
    
    print("✅ Bot siap. Menjalankan polling...")
    app.run_polling()

if __name__ == "__main__":
    main()
