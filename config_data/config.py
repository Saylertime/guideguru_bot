import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
USERKEY_TEXT_RU = os.getenv("USERKEY_TEXT_RU")


DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("eldo", "Правила для Эльдорадо"),
    ("mvideo", "Правила для Мвидео"),
    ("free_texts", "Свободные брифы"),
    ("check", "Проверить текст на стоп-слова"),
    ("unique", "Проверить текст на уникальность"),
    ("history", "Все тексты за этот месяц"),
    ("last_month", "Все тексты за прошлый месяц"),
    ("all_texts", "Все тексты с ноября 2023 года"),
)
