# Aplikacja do Losowania Pytań na Egzamin Dyplomowy

Aplikacja napisana w Pythonie z wykorzystaniem biblioteki `customtkinter`. Umożliwia losowanie pytań egzaminacyjnych dla studentów różnych kierunków i specjalizacji wydziału Budownictwa i Inżynierii Środowiska SGGW.

## Funkcjonalności

- Wybór stopnia studiów (I stopień, II stopień).
- Losowanie pytań ogólnych i specjalizacyjnych.
- Dynamiczne generowanie przycisków dla dostępnych kierunków i specjalizacji.
- Ekran wynikowy prezentujący wylosowane pytania dla dokonanego wyboru przez użytkownika.

## Wymagania

- Python 3.8 lub nowszy
- Zainstalowana biblioteka `customtkinter`

## Instalacja
1. Sklonuj repozytorium lub pobierz pliki projektu, możesz zrobić to za pomocą polecenia: 
    ```bash
    git clone https://github.com/romateusz/wbis_losowanie_pytan_dyplomowych.git
    ```

2. Upewnij się, że masz zainstalowanego Pythona. [Pobierz Pythona](https://www.python.org/downloads/)
3. Zainstaluj wymagane biblioteki za pomocą polecenia:

   ```bash
   pip install -r requirements.txt

## Jak uruchomić?

Przed uruchomienem upewnij się, że wszystkie pliki `.txt` z pytaniami znajdują się w odpowiednich katalogach:
   - `./st_I/` dla kierunków I stopnia
   - `./st_II/og/` dla ogólnych pytań II stopnia
   - `./st_II/spec/` dla specjalizacyjnych pytań II stopnia

## Struktura Plików

```
|-- st_I/
|   |-- Architektura_krajobrazu.txt
|   |-- Budownictwo.txt
|   |-- ...
|-- st_II/
|   |-- og/
|   |   |-- Architektura krajobrazu.txt
|   |   |-- Budownictwo.txt
|   |   |-- ...
|   |-- spec/
|       |-- Architektura_krajobrazu/
|       |   |-- Projektowanie krajobrazu.txt
|       |   |-- ...
|       |-- ...
|-- alped.py
|-- requirements.txt
|-- README.md
```

## Uruchamianie na Windows i Linux

### Windows
1. Otwórz wiersz poleceń (Command Prompt) lub terminal w katalogu, w którym znajduje się projekt.
2. Uruchom aplikację za pomocą polecenia:
   ```bash
   python alped.py
   ```

### Linux
1. Otwórz terminal i przejdź do katalogu projektu
2. Upewnij się, że Python jest zainstalowany, wpisując:
   ```bash
   python3 --version
   ```
   Jeśli polecenie zwraca wersję Pythona, możesz przejść dalej. Jeśli nie, zainstaluj Pythona używając menedżera pakietów, np.:
   ```bash
   sudo apt install python3
   ```
3. Uruchom aplikację za pomocą polecenia:
   ```bash
   python3 alped.py
   ```

## Autor

Mateusz Roman

## Licencja

Ten projekt jest dostępny na licencji MIT. Szczegóły w pliku `LICENSE`.
