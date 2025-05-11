import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "به ربات ClickCinema خوش آمدید! برای دریافت فیلم‌ها، روی دکمه زیر کلیک کنید.",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("دانلود فیلم", callback_data="get_files")]])
    )

async def get_files(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    files = [
        ("کیفیت 240", "https://t.me/ClickCinema/947"),
        ("کیفیت 360", "https://t.me/ClickCinema/947"),
        ("کیفیت 480", "https://t.me/ClickCinema/947"),
        ("کیفیت 720", "https://t.me/ClickCinema/947"),
        ("کیفیت 1080", "https://t.me/ClickCinema/947"),
    ]

    for quality, link in files:
        msg = await query.message.reply_text(f"{quality}:\n{link}")
        await asyncio.sleep(120)
        try:
            await context.bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
        except:
            pass

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(get_files, pattern="get_files"))
    app.run_polling()
