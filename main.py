from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Bot alive!")

updater = Updater("8071457191:AAFfAixXkkp8Oqg379Eysjfeo-ceomzcOvw", use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
