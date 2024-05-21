import telebot
import dotenv
import django
import os
import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_server.settings")
django.setup()

from object_creator import create_user, create_message
#Получаем токен из окружения
dotenv.load_dotenv()
tg_token = os.environ['tgtoken']

#Инициализируем телеграм бота с помощью токена
diplom_bot = telebot.TeleBot(tg_token)

#Функция ждет сообщения из тг и обрабатывает их
@diplom_bot.message_handler(content_types=["text"])
def message_handler(message: callable) -> None:
    user_id = message.from_user.id
    user_text = message.text.strip()
    user_name = message.from_user.first_name
    user = create_user(user_id, user_name)
    create_message(user = user[0], sender = "user", text = user_text, date = "2024-10-06 23:23")


#В эту функцию нужно передать айди юзера телеграм и сообщение, оно отправится ему в телеграм
def send_message(id,answer):
    diplom_bot.send_message(id, answer)

#Код который запустится при старте программы
if __name__ == "__main__":
    try:
        print('bot polling started')
        diplom_bot.infinity_polling(skip_pending=True, none_stop=True)
    except Exception as e:
        print(f"An error occurred: {e}")