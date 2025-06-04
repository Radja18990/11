import requests
import config

def alert_admin(message):
    text = f"❗️Новый вопрос без ответа: {message}"
    url = f"https://api.telegram.org/bot{config.TG_BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": config.ADMIN_CHAT_ID, "text": text})
