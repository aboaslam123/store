from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('مرحباً بك في متجر شحن الألعاب!')
if __name__ == '__main__':
    application = ApplicationBuilder().token("8946067667:AAHC_bsaom3m3HaS31cX8lUyaEE4Qn7Z5uI").build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

