from loader import bot
from keyboards.reply.create_markup import create_markup_with_url

@bot.message_handler(commands=['eldo'])
def eldo(message):

      buttons = [
            ('Каталог товаров одной категории',
             'https://docs.google.com/document/d/1fHq-6PgdLUkE6X9HK0SRK-8t30DSFTSVPJDmKdAx3B4/edit?usp=sharing', None),
            ('Каталог товаров разных категорий одной темы',
             'https://docs.google.com/document/d/1y0wSO_djj64380iLUP0kzGosVONEBY7_AH-_X2ujX9o/edit?usp=sharing', None),
            ('Подборка игр',
             'https://docs.google.com/document/d/1APRK4fEmrre6aPKndO86LwfMozFTLtuivjjR-Iwsyrs/edit?usp=sharing', None),
            ('Подборка фильмов',
             'https://docs.google.com/document/d/1emGeHb3P9byR7nS8HmmbwpXBfFedsMAxsqyeH4dwfGc/edit?usp=sharing', None),
            ('Интервью',
             'https://docs.google.com/document/d/1QMDgODzF2B5ZjvmohtOHph9OwbpqvhOvuCSzuM1pzGE/edit?usp=sharing', None),
            ('Разговор с экспертом',
             'https://docs.google.com/document/d/1_ZwRDlHrpsLXsJAnp1HiKSbCJwMNLRKl9W2LPQ9VSp4/edit?usp=sharing', None),
            ('Каталог товаров с историями пользователей',
             'https://docs.google.com/document/d/1hsKtCah9NoWdrfSrgipdLoH-1EMCdivchj8f4Q9E0g4/edit?usp=sharing', None),
            ('Что известно о фильме',
             'https://docs.google.com/document/d/1Abv76Dt4q4HZ8ZGUACp5h0UmvpXgKb17ADp_oUAhvWw/edit?usp=sharing', None),
            ('Что известно об игре (Предрелизный обзор)',
             'https://docs.google.com/document/d/1bVHas6FMBO76DwccE0Tv5-UhazvyLc7w9BvCbdR4RN0/edit?usp=sharing', None),
            ('Рецепт',
             'https://docs.google.com/document/d/1gx5PVTaLeSBgU3tFLBlVhsJ8CS0z_41E-9dZTV2mhFQ/edit?usp=sharing', None),
            ('Советы, помощь, инструкции, пояснения',
             'https://docs.google.com/document/d/1JJ17im1Q6-6QEGWKoUx7o5tZ0YcPjrSqMQ0xb4-1z-0/edit?usp=sharing', None),
            ('Подборка подарков',
             'https://docs.google.com/document/d/1Uk9eUIydKiZ3IM-_tyKbNqMyHNlgahPl9gEHqBENwDk/edit?usp=sharing', None),
            ('Обзор смартфона',
             'https://docs.google.com/document/d/1MMHw17-4F7-xcdvOrZJYK8r7B-jOWu2ClznL-XbLDl4/edit?usp=sharing', None),
            ('⬆⬆⬆ НАЗАД В МЕНЮ ⬆⬆⬆', None, 'start'),

      ]
      markup = create_markup_with_url(buttons)
      bot.send_message(message.from_user.id, "Выберите, что хотите", reply_markup=markup)

      # msg = f"<b>КАК ОФОРМЛЯТЬ МАТЕРИАЛЫ ДЛЯ ЭЛЬДОБЛОГА</b>\n\n\n" \
    #       f"<a href='https://docs.google.com/document/d/1fHq-6PgdLUkE6X9HK0SRK-8t30DSFTSVPJDmKdAx3B4/edit?usp=sharing'><b>Каталог товаров одной категории</b></a>\n\n" \
    #       f"<a href='https://docs.google.com/document/d/1y0wSO_djj64380iLUP0kzGosVONEBY7_AH-_X2ujX9o/edit?usp=sharing'><b>Каталог товаров разных категорий одной темы</b></a>\n\n" \
    #       f"<a href='https://docs.google.com/document/d/1APRK4fEmrre6aPKndO86LwfMozFTLtuivjjR-Iwsyrs/edit?usp=sharing'><b>Подборка игр</b></a>\n\n" \
    #       f"<a href='https://docs.google.com/document/d/1emGeHb3P9byR7nS8HmmbwpXBfFedsMAxsqyeH4dwfGc/edit?usp=sharing'><b>Подборка фильмов</b></a>\n\n" \
    #       f"<a href='https://docs.google.com/document/d/1QMDgODzF2B5ZjvmohtOHph9OwbpqvhOvuCSzuM1pzGE/edit?usp=sharing'><b>Интервью</b></a>\n\n" \
    #       f"<a href='https://docs.google.com/document/d/1_ZwRDlHrpsLXsJAnp1HiKSbCJwMNLRKl9W2LPQ9VSp4/edit?usp=sharing'><b>Разговор с экспертом</b></a>\n\n" \
    #       f"<a href='https://docs.google.com/document/d/1hsKtCah9NoWdrfSrgipdLoH-1EMCdivchj8f4Q9E0g4/edit?usp=sharing'><b>Каталог товаров с историями пользователей</b></a>\n\n" \
    #       f"<a href='https://docs.google.com/document/d/1Abv76Dt4q4HZ8ZGUACp5h0UmvpXgKb17ADp_oUAhvWw/edit?usp=sharing'><b>Что известно о фильме</b></a>\n\n" \
    #       f"<a href='https://docs.google.com/document/d/1bVHas6FMBO76DwccE0Tv5-UhazvyLc7w9BvCbdR4RN0/edit?usp=sharing'><b>Что известно об игре (Предрелизный обзор)</b></a>\n\n" \
    #       f"<a href='https://docs.google.com/document/d/1gx5PVTaLeSBgU3tFLBlVhsJ8CS0z_41E-9dZTV2mhFQ/edit?usp=sharing'><b>Рецепт</b></a>\n\n" \
    #       f"<a href='https://docs.google.com/document/d/1JJ17im1Q6-6QEGWKoUx7o5tZ0YcPjrSqMQ0xb4-1z-0/edit?usp=sharing'><b>Советы, помощь, инструкции, пояснения</b></a>\n\n" \
    #       f"<a href='https://docs.google.com/document/d/1Uk9eUIydKiZ3IM-_tyKbNqMyHNlgahPl9gEHqBENwDk/edit?usp=sharing'><b>Подборка подарков</b></a>\n\n" \
    #       f"<a href='https://docs.google.com/document/d/1MMHw17-4F7-xcdvOrZJYK8r7B-jOWu2ClznL-XbLDl4/edit?usp=sharing'><b>Обзор смартфона</b></a>\n\n" \

    # bot.send_message(message.chat.id, msg, parse_mode='HTML', disable_web_page_preview=True)

# f"<a href=''><b></b></a>\n\n"
