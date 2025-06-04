import requests
import config

def get_new_messages():
    headers = {"Client-Id": config.OZON_CLIENT_ID, "Api-Key": config.OZON_API_KEY}
    # Пример: заглушка, верни тестовые сообщения
    return [{"chat_id": "123456", "text": "где инструкция"}]

def send_answer(chat_id, message):
    headers = {"Client-Id": config.OZON_CLIENT_ID, "Api-Key": config.OZON_API_KEY}
    print(f"Ответ отправлен в Ozon: {message} (чат {chat_id})")
