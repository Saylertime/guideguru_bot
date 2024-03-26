from loader import bot
from utils.sheets import all_texts_of_author

@bot.message_handler(commands=['all_texts'])
def all_texts(message):
    username = message.from_user.username
    all_texts_eldo, all_texts_mvideo = all_texts_of_author(username)
    if all_texts_eldo:
        with open(all_texts_eldo, 'rb') as file:
            bot.send_document(message.chat.id, file)
    if all_texts_mvideo:
        with open(all_texts_mvideo, 'rb') as file:
            bot.send_document(message.chat.id, file)
    if not all_texts_eldo and not all_texts_mvideo:
        msg = "Ничего не нашел. У тебя точно есть тексты?"
        bot.send_message(message.chat.id, msg)
    bot.delete_state(message.chat.id)
