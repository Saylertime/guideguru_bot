from loader import bot
from utils.docs import check_text
from states.overall import OverallState

@bot.message_handler(commands=['check'])
def check(message):
    bot.send_message(message.from_user.id, 'Кидай ссылку на документ, который надо проверить.\n\n '
                                      'Ссылка должна выглядеть так.\n\n'
                                      'https://docs.google.com/document/d/136QHaIF8G_w6fJzTJIstoA0sKRwNElsTAzzXyJ0xwj8/edit')
    bot.set_state(message.from_user.id, state=OverallState.check)

@bot.message_handler(state=OverallState.check)
def check_answer(message):
    try:
        url = message.text.split('/')[-2]
        answer = check_text(url)
        bot.send_message(message.from_user.id, answer)
    except:
        bot.send_message(message.from_user.id, 'Похоже, ссылкая кривая или формат не тот')
    finally:
        bot.delete_state(message.from_user.id)


