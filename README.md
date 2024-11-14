# Zadanie programowe - rekrutacja

## Kila słów od autora

Początkowym zadaniem było stworzenie prostej aplikacji używając w tym celu języka Python lub JavaScript w celu szeroko pojętej modyfikacji pliku tekstowego. Nie ukrywam, stworzenie zadowalającego mnie kodu spełniające wszelkie wymogi nie zajęło mi dużo czasu, więc skupiłem się bardziej nad zadaniem dodatkowym, natomiast nie byłbym sobą, gdybym nie stworzył zadania dodatkowego... do zadania dodatkowego :) 

Amianowicie początkowo mając już stworzony przez AI `artykul.html`, przygotowałem zarówno szablon jak i podgląd zgodnie z poleceniem. Natomiast, żeby lepiej przedstawić dany artykuł, wykonałem podstawową stronę, wyimaginowanej firmy o nazwie XYZ, na której treść tego artykułu się znalazła. Idąc dalej, strona wyglądała w moich oczach trochę pusto, więc za pomocą sztucznej inteligencji stworzyłem grafiki, korzystając z promptów wygenerowanych w pliku `artykul.html`, oraz logo dla firmy XYZ. 

[Pełna strona](https://bartoszwer1.github.io/oxido-rekrutacja-podglad.github.io/) - tutaj znajuje się powyżej omawiana pełna strona, określona mianem dodatkowego zadania do zadania dodatkowego.
   [Repozytorium](https://github.com/bartoszwer1/oxido-rekrutacja-podglad.github.io) - tutaj znajdują się wszystkie pliki, składające się na całokształt pełnej strony

Jeśli chodzi o zadanie dla chętnych - w poniżej podlinkowanym repozytorium znajdują się dwa pliki: `szablon.html` oraz `podglad.html`. Jeśli dobrze zrozumiałem to tutaj już można było zastosować CSS oraz JavaScript, natomiast w repozytorium wraz z plikami `.html`, nie mogło się nic więcej już znaleźć, zatem umieściłem kod CSS bezpośrednio w pliku `.html`. JavaScript uważam, że do wyświetlenia artykułu samego w sobie nie był aż tak potrzebny, w przeciwieństwie do [Pełnej strony](https://bartoszwer1.github.io/oxido-rekrutacja-podglad.github.io/).

   [Repozytorium zadanie dodatkowe](https://github.com/bartoszwer1/oxido-rekrutacja-dodatkowe)

## Opis działania

Aplikacja wczytuje tekst artykułu z pliku `tekst.txt`, następnie wysyła go wraz z odpowiednim promptem do modelu OpenAI. W odpowiedzi otrzymuje kod HTML zgodny z podanymi wytycznymi, który zapisuje w pliku `artykul.html`.

Dodatkowo, przygotowany jest szablon `szablon.html`, służący do podglądu wygenerowanego artykułu oraz pełny podgląd w pliku `podgląd.html` lub w postaci pełnej strony imitującej artykuł firmy XYZ zajmującej się sztuczną inteligencją pod linkiem [XYZ](https://bartoszwer1.github.io/oxido-rekrutacja-podglad.github.io/)

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


