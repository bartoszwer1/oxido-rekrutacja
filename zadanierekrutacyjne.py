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
- Popraw tekst artykułu tak aby usunąć znaki wynikające z konwersji pliku takie jak Ä‡ Å¼ Ä™ Ä™
- Użyj odpowiednich tagów HTML do strukturyzacji treści.
- Określ miejsca, gdzie warto wstawić grafiki – oznacz je z użyciem tagu <img> z atrybutem src="image_placeholder.jpg". Dodaj atrybut alt do każdego obrazka z dokładnym promptem, który możemy użyć do wygenerowania grafiki. Umieść podpisy pod grafikami używając odpowiedniego tagu HTML.
- Nie dodawaj kodu CSS ani JavaScript. Zwróć tylko kod do wstawienia pomiędzy <body> i </body>. Nie dołączaj znaczników <html>, <head> ani <body>.
- Nie dodawaj do wygenerowanego pliku znaczników takich jak ```html.
"""
    },
    {
        "role": "user",
        "content": f"Tekst artykułu:\n{tekst_artykulu}\n\nWygeneruj kod HTML:"
    }
]

# Wywołanie API ChatCompletion, stworzenie odpowiedzi, określenie modelu, przekazanie promptu
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
