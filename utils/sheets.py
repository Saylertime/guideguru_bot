from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from utils.calend import current_month
import os


SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SAMPLE_SPREADSHEET_ID = "14rfetnaiqgiT3o0TsLC-yi3EICobIH5rNljilhDS70M"

creds = None
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
        token.write(creds.to_json())

def get_data_from_sheet(month):
    SAMPLE_RANGE_NAME = f"{month}!A2:I"

    try:
        service = build("sheets", "v4", credentials=creds)

        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return None

        return values

    except HttpError as err:
        print(err)
        return None


all_authors = {
    'quir1ll': 'Кирилл',
    'kirill_morales': 'Моралес',
    'isaywheee': 'Саша',
    'Vice_Mallow': 'Артем',
    'Catygen': 'Генералова',
    'interneuronic': 'Дина',
    'baego': 'Егор',
    'ArseniyMirniy': 'Арсений',
    'Mkarow': 'Вадим',
    'Irina_Grodzinskaya': 'Ира',
    'annacalico': 'Анна',
    'aliullov_sh': 'Шамиль',
    'the_barteneva': 'Ана',
    'johnyscreams': 'Бо',
    'barvikki': 'Вика',
    'pescadotravel': 'Сергей',
    'suspicious_fox': 'Алина',
    'kuchkanov': 'Фил',
    'Sedn04ka': 'Седна',
    'Hurtson': 'Никита',
    'dimkor42': 'Дима',
    'drrmmn': 'Дарья',
    'marabouto': 'Рома',
    'vegur': 'Ксения',
    'saylertime': 'Глинкин',
    'maria_vyshnegradskaya': 'Маша'
}


def rep_name_and_month(username, month='Март 2024'):
    values = get_data_from_sheet(month)
    name = all_authors.get(username)
    if not values:
        return
    try:
        dct = dict()
        dct_texts = dict()
        texts_in_work = dict()
        texts_in_work[name] = []
        for row in values:
            try:
                title = f"{row[0]} — {row[6]} руб. {row[1]}"
                money = int(row[6])
                link = row[1]
                brief = str(row[3])
                if name == row[2]:
                    if (name in dct or name in dct_texts):
                        if link:
                            value_money, current_count = dct[name]
                            dct_texts[name].append(title)
                            dct[name] = (value_money + money, current_count + 1)
                        else:
                            texts_in_work[name].append((title, brief))
                    else:
                        dct[name] = (money, 1)
                        dct_texts[name] = [title]
            except:
                pass
        msg = ''
        sorted_dct = sorted(dct.items(), key=lambda item: item[1][0], reverse=True)
        for author, summa in sorted_dct:
            msg += f"Гонорар за сданные тексты за {month} — {summa[0]} руб.\nТекстов за месяц — {summa[1]}\n\n"

        msg_texts = '<b>Все сданные тексты:</b> \n'
        for title in dct_texts[name]:
            msg_texts += f"\n— {title}\n"
        msg += msg_texts

        if texts_in_work[name]:
            msg_texts_in_work = '\n\n<b>Тексты в работе: </b>\n'
            for title in texts_in_work[name]:
                msg_texts_in_work += f"\n— <a href='{title[1]}'>{title[0]}</a>\n"
            msg += msg_texts_in_work

        if len(msg) > 4090:
            msg_file = create_and_return_file(name, 'last_month', msg)
            return msg_file
        else:
            return msg

    except:
        msg = 'Кажется, у тебя пока ничего не написано...'

        return msg


def all_texts_of_author(username):
    name = all_authors.get(username)
    all_months = ["Ноябрь 2023", "Декабрь 2023", "Январь 2024", "Февраль 2024", "Март 2024"]
    temp_eldo = ""
    temp_mvideo = ""
    recording_mvideo = False

    for month in all_months:
        values = get_data_from_sheet(month)
        if not values:
            return

        msg_texts_eldo = ''
        msg_texts_mvideo = ''
        for row in values:
            if 'МВИДЕО' in str(row):
                recording_mvideo = True
            try:
                title = f"{row[0]} — {row[1]}"
                link = row[1]
                if name == row[2] and link:
                    if recording_mvideo:
                        msg_texts_mvideo += f"\n{title}\n"
                    else:
                        msg_texts_eldo += f"\n{title}\n"
            except:
                pass

        temp_eldo += msg_texts_eldo
        temp_mvideo += msg_texts_mvideo

        recording_mvideo = False

    temp_file_eldo = create_and_return_file(name, 'eldo', temp_eldo)
    temp_file_mvideo = create_and_return_file(name, 'mvideo', temp_mvideo)

    temp_eldo = ''
    temp_mvideo = ''

    return temp_file_eldo, temp_file_mvideo


def create_and_return_file(name, blog, content):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    temp_directory = os.path.join(current_directory, "temp")
    os.makedirs(temp_directory, exist_ok=True)
    file_path = os.path.join(temp_directory, f"{name}_{blog}.txt")
    with open(file_path, "w") as file:
        if content:
            file.write(content)
            return file_path
        else:
            return ''


def brief_is_free():
    values = get_data_from_sheet(current_month())
    if not values:
        return

    all_briefs = []
    flag_mvideo = False

    for row in values:
        if "МВИДЕО" in str(row):
            flag_mvideo = True
        try:
            title = str(row[0])
            brief = str(row[3])
            author = row[2]
            money = str(row[6])
            symbs = str(row[8])

            if brief and not author:
                temp_row = f'[{title}]({brief})\n' \
                           f'Объем: {symbs} тыс. символов\n' \
                           f'Для блога: {"Мвидео" if flag_mvideo else "Эльдорадо"}\n' \
                           f'Гонорар: {money}\n\n'
                all_briefs.append(temp_row)

        except Exception as e:
            print(f"Error: {e}")

    msg = ''
    for num, brief in enumerate(all_briefs, start=1):
        msg += f"{num}. {brief}"

    return msg
