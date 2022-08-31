from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *


updater = Updater('5555915955:AAGtohvkckHmBWS0uwk1o2uqTnC1WUuRe1M')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
print('server start')
updater.start_polling()
updater.idle()