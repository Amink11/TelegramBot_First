"""
author : Amink11
Description : Telegram bot
Date_of_Develope : 1400-07-29 / 21 oct 2021
second develope : 1400-08-09 / 31 oct 2021
Date_Of_release :
"""


from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import logging


updater = Updater(token='2099981011:AAEFGqZcvGMcO782cxDlIBR7gzZIlikLoxE')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#functions go here

#adding answer to start command
def start(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="به ربات اکو خوش آمدید")
#adding answer to choose command
def choose(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please choose one of these!")
#echo everything you send
def echo(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Your message is : " + update.message.text)
#aaa
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

#handlers go here

start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)

choose_handler = CommandHandler('choose',choose)
dispatcher.add_handler(choose_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

caps_handler=CommandHandler('caps',caps)
dispatcher.add_handler(choose_handler)

updater.start_polling()



