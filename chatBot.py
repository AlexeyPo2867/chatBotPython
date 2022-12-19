from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

# moscow_my_Bot - Бот в Телеграме
# myBot - username

app = Updater("5881762588:AAHo_i9FeeCb-qvee3GQbpruXsqG6P1mmcc")

# hello - имя команды в Телеграмм (запускается - /hello, /time, /help/ /sum)
# hello_command, time_command, help_command, sum_command - функции которые вызываются пр наборе 
# комманд - /hello, /time, /help, /sum

app.dispatcher.add_handler(CommandHandler("hello", hello_command)) 
app.dispatcher.add_handler(CommandHandler("time", time_command))
app.dispatcher.add_handler(CommandHandler("help", help_command))
app.dispatcher.add_handler(CommandHandler("sum", sum_command))

print("Сервер запущен")
app.start_polling()
app.idle()