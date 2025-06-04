import time
from ozon_api import get_new_messages, send_answer
from telegram_alerts import alert_admin
from utils import find_answer
from gpt_engine import get_gpt_answer
import config

def main_loop():
    while True:
        messages = get_new_messages()
        for msg in messages:
            question = msg.get("text", "").lower()
            answer = find_answer(question)
            if not answer:
                answer = get_gpt_answer(question)
                if not answer:
                    alert_admin(question)
                    continue
            send_answer(msg["chat_id"], answer)
        time.sleep(30)

if __name__ == "__main__":
    main_loop()
