from openai import OpenAI
import openai
import os
client = OpenAI()

# Ustawienie klucza API
openai.api_key = os.getenv('OPENAI_API_KEY')

# Wczytanie artykułu z pliku (dla nazwy: tekst.txt)
with open('tekst.txt', 'r', encoding='utf-8') as file:
    tekst_artykulu = file.read()

# Przygotowanie wiadomości dla modelu OpenAI, 
# określenie charakteru odpowiedzi i treści użytkownika - w tym przypadku artykul
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

# Wywołanie API CharCompletion, stworzenie odpowiedzi, określenie modelu, przekazanie promptu
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
)

# Zapisanie odpowiedzi, będącej kodem HTML
kod_html = response.choices[0].message.content

# Zapisanie kodu HTML do pliku
with open('artykul.html', 'w', encoding='utf-8') as file:
    file.write(kod_html)

# Wyświetlenie informacji zwrotnej dla użytkownika
print("Wygenerowano plik artykul.html")
