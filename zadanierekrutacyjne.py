from openai import OpenAI
import openai
import os
client = OpenAI()

openai.api_key = os.getenv('OPENAI_API_KEY')

with open('tekst.txt', 'r', encoding='utf-8') as file:
    tekst_artykulu = file.read()

messages = [
    {
        "role": "system",
        "content": """
Przekształć poniższy tekst artykułu na kod HTML zgodnie z następującymi wytycznymi:

"""
    },
    {
        "role": "user",
        "content": f"Tekst artykułu:\n{tekst_artykulu}\n\nWygeneruj kod HTML:"
    }
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
)

kod_html = response.choices[0].message.content

with open('artykul.html', 'w', encoding='utf-8') as file:
    file.write(kod_html)
