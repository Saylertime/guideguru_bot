from loader import bot
from utils.sheets import brief_is_free

@bot.message_handler(commands=['free_texts'])
def free_texts(message):
    free_authors = brief_is_free()
    if free_authors:
        msg = f'Сейчас свободны: \n\n' \
              f'{free_authors}'
    else:
        msg = 'Всё разобрали! Ждём новых поступлений'

    bot.send_message(message.from_user.id, msg, parse_mode='Markdown', disable_web_page_preview=True)
