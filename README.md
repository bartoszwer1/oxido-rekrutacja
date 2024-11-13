# Zadanie programowe - instrukcja uruchomienia 

## Opis działania

Aplikacja wczytuje tekst artykułu z pliku 'tekst.txt', następnie wysyła go wraz z odpowiednim promptem do modelu OpenAI. W odpowiedzi otrzymuje kod HTML zgodny z podanymi wytycznymi, który zapisuje w pliku 'artykul.html'.

Dodatkowo, przygotowany jest szablon 'szablon.html', służący do podglądu artykułu oraz pełny podgląd w pliku 'podgląd.html'. Całość znajduje się pod linkiem:

[Podgląd zrealizowanego programu](https://bartoszwer1.github.io/oxido-rekrutacja-podglad.github.io/)

[Link do repozytorium - kod źródłowy szablonu i podglądu](https://github.com/bartoszwer1/oxido-rekrutacja-podglad.github.io)

## Instrukcja uruchomienia

1. **Pobieranie klucza API OpenAI:**
   - Należy zarejestrować się lub zalogować na stronie [OpenAI](https://beta.openai.com/).
   - Następnie należy przejść do sekcji [API Keys](https://platform.openai.com/account/api-keys).
   - Postępując zgodnie z instrukcjami należy wygenerować nowy klucz API.

2. **Konfiguracja środowiska Python:**
   - Należy upewnić się, że jest zainstalowany Python 3.x.
   - (Opcjonalnie) Utwórzyć i aktywować wirtualne środowisko:
     ```bash
     python -m venv venv
     source venv/bin/activate  # Linux/MacOS
     venv\Scripts\activate     # Windows
     ```
   - Zainstalować bibliotekę `openai`:
     ```bash
     pip install openai
     ```

3. **Konfiguracja aplikacji:**
   - Należy przejść do katalogu w którym zapisano plik `zadanierekrutacyjne.py`.
   - W oknie terminala należy wprowadzić komendę:
     ```bash
     export OPENAI_API_KEY='TWÓJ_KLUCZ_API'
     ```
   - Podczas wprowadzania powyżej komendy należy zastąpić `'TWÓJ_KLUCZ_API'` prawidłowym kluczem wygenerowanym zgodnie z instrukcją w punkcie 1.

5. **Uruchamianie aplikacji:**
   ```bash
   python zadanierekrutacyjne.py
   ```
   lub
   ```bash
   python3 zadanierekrutacyjne.py
   ```
   Po uruchomieniu aplikacji należy poczekać na zakończenie pracy programu. 
   Zakończenie działania programu zostanie zwróceniem informacji:
   ```bash
   Wygenerowano plik artykul.html
   ```

6. **Podgląd pliku:**

W celu sprawdzenia zawartości wygenerowanego pliku, należy go uruchomić (domyślnie odbywa się to za pośrednictwem przeglądarki internetowej lub edytora tekstu), lub można skorzystać z programu podglądowego, do którego link znajduje się powyżej w opisie działania.


