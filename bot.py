"""
author : Amink11
Description : Telegram bot
Date_of_Develope : 1400-07-29 / 21 oct 2021
Date_Of_release :
"""


from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import logging


updater = Updater(token='2099981011:AAEFGqZcvGMcO782cxDlIBR7gzZIlikLoxE', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#functions goes here

#adding answer to start command
def start(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="به ربات اکو خوش آمدید")
#adding answer to choose command
def choose(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please choose one of these!")
#echo everything you send
def echo(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

#handlers goes here

start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)

choose_handler = CommandHandler('choose',choose)
dispatcher.add_handler(choose_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)



updater.start_polling()



