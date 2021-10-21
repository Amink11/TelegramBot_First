from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging


updater = Updater(token='2099981011:AAEFGqZcvGMcO782cxDlIBR7gzZIlikLoxE', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
#adding answer to start command
def start(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my first bot!")
#adding answer to choose command
def choose(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please choose one of these!")

start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)

start_handler1 = CommandHandler('choose',choose)
dispatcher.add_handler(start_handler1)

updater.start_polling()



