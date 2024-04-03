from loader import bot
from utils.sheets import all_texts_of_author
from utils.logger import logger

@bot.message_handler(commands=['all_texts'])
def all_texts(message):
    logger.warning(f'{message.from_user.username} — команда ALL_TEXTS')
    username = message.from_user.username
    all_texts_eldo, all_texts_mvideo = all_texts_of_author(username)
    if all_texts_eldo:
        with open(all_texts_eldo, 'rb') as file:
            bot.send_document(message.from_user.id, file)
    if all_texts_mvideo:
        with open(all_texts_mvideo, 'rb') as file:
            bot.send_document(message.from_user.id, file)
    if not all_texts_eldo and not all_texts_mvideo:
        msg = "Ничего не нашел. У тебя точно есть тексты?"
        bot.send_message(message.from_user.id, msg)
    bot.delete_state(message.from_user.id)
