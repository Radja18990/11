import openai
import config

openai.api_key = config.OPENAI_API_KEY

def get_gpt_answer(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            max_tokens=200,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("Ошибка GPT:", e)
        return None
