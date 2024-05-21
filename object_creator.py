import dotenv
dotenv.load_dotenv()
import django
django.setup()
from tg_app.models import user_model, message_model

def create_user(user_id, user_name):
    user = user_model.objects.get_or_create(user_id = user_id, user_name = user_name)
    return user

def create_message(user, sender, text, date):
    user_message = message_model.objects.create(message_date = date, message_text = text, user = user, sender = sender)
    return user_message
