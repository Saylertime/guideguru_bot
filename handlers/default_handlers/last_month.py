from loader import bot
from utils.sheets import rep_name_and_month
from utils.calend import previous_month
import os

@bot.message_handler(commands=['last_month'])
def last_month(message):
    username = message.from_user.username
    msg = rep_name_and_month(username, previous_month())
    if os.path.isfile(msg):
        with open(msg, 'rb') as file:
            bot.send_document(message.from_user.id, file)
    else:
        try:
            bot.send_message(message.from_user.id, msg, parse_mode='HTML')
        except Exception as e:
            bot.send_message(message.from_user.id, e)
