import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from common_methods import *
from morra_cinese import *


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

BOT_TOKEN

def main():

    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # hanlder per la funzione di saluto
    hello_handler = CommandHandler('saluti', saluti)
    dispatcher.add_handler(hello_handler)

    updater.start_polling()

    # handler per la morra cinese
    morra_cinese_handler = CommandHandler('morra', morra)
    dispatcher.add_handler(morra_cinese_handler)
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    # hanlder per quando non riconosce un comando 
    unknown_handler = MessageHandler(Filters.command, unknown_command)
    dispatcher.add_handler(unknown_handler)

  


main()
