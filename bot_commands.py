from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *

def hello_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Привет {update.effective_user.first_name} !')

def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Время {datetime.datetime.now().time()} !')

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hello\n/time\n/help\n/sum\n')

def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg=update.message.text
    items=msg.split() #/sum x y
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'Сумма {x} + {y} = {x + y} !')