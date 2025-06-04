import json

def load_faq():
    with open("faq.json", "r", encoding="utf-8") as f:
        return json.load(f)

FAQ = load_faq()

def find_answer(question):
    for keyword, answer in FAQ.items():
        if keyword in question:
            return answer
    return None
