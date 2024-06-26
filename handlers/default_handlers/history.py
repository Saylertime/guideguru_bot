from loader import bot
from utils.sheets import rep_name_and_month
from utils.logger import logger

@bot.message_handler(commands=['history'])
def history(message):
    logger.warning(f'{message.from_user.username} — команда HISTORY')
    username = message.from_user.username
    print(username)
    msg = rep_name_and_month(username)
    bot.send_message(message.from_user.id, msg, parse_mode='HTML')
