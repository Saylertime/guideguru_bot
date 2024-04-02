from loader import bot
from utils.sheets import rep_name_and_month
from utils.calend import history_file

@bot.message_handler(commands=['history'])
def history(message):
    history_file(message.from_user.username, 'history')
    username = message.from_user.username
    print(username)
    msg = rep_name_and_month(username)
    bot.send_message(message.from_user.id, msg, parse_mode='HTML')
