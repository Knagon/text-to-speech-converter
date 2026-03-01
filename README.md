Poniżej masz **pełną ocenę projektu** oraz **profesjonalny README.md** w takim samym stylu jak poprzednie (ML + Turtle Crossing).  
Możesz wkleić go 1:1 do GitHuba.

---

# ✔️ Czy projekt nadaje się do portfolio?

**Tak — bardzo.**

To jest projekt:

- z GUI (tkinter + ttkbootstrap),
- z realną funkcjonalnością (Text‑To‑Speech),
- wykorzystujący **asynchroniczność (asyncio)**,
- korzystający z **wielowątkowości (threading)**,
- używający zewnętrznej biblioteki **edge‑tts** (Microsoft Azure TTS),
- z paskiem postępu i dynamicznym UI,
- z obsługą zdarzeń i logiką czasu.

To wygląda **dużo bardziej profesjonalnie** niż typowe projekty początkujących.

Nadaje się idealnie jako projekt portfolio, szczególnie w kategorii:

**„Python Desktop App – Text‑to‑Speech Converter”**

---

# 📄 GOTOWY README.md (profesjonalny, bez emotek, w stylu poprzednich)

Wklej poniższy tekst do pliku `README.md`.

---

## Konwerter tekstu na mowę (Python + TTS)

Aplikacja desktopowa napisana w Pythonie, wykorzystująca bibliotekę **edge‑tts** do konwersji tekstu na mowę z użyciem neuralnych głosów Microsoft Azure. Program posiada graficzny interfejs użytkownika oparty na **tkinter + ttkbootstrap**, obsługuje wielowątkowość oraz prezentuje postęp działania w czasie rzeczywistym.

---

## Cel projektu

Celem projektu jest stworzenie funkcjonalnego narzędzia, które:

- konwertuje tekst na plik audio MP3,
- pozwala wybrać głos i język syntezy mowy,
- wyświetla przewidywany czas trwania operacji,
- pokazuje pasek postępu w trakcie generowania audio,
- automatycznie odtwarza wygenerowany plik,
- posiada przejrzysty interfejs graficzny.

Projekt prezentuje umiejętność pracy z GUI, programowaniem asynchronicznym, wielowątkowością oraz integracją z zewnętrznymi usługami TTS.

---

## Technologie

- **Python 3**
- **tkinter + ttkbootstrap** – interfejs graficzny
- **edge‑tts** – synteza mowy (Microsoft Azure Neural Voices)
- **asyncio** – obsługa asynchroniczna
- **threading** – wykonywanie TTS w tle
- **subprocess** – automatyczne odtwarzanie pliku MP3

---

## Zrzuty ekranu

### Główne okno aplikacji

![GUI](images/GUI.png)
*Widok głównego interfejsu aplikacji: pole tekstowe do wprowadzania treści, wybór głosu syntezy mowy, przycisk uruchamiający konwersję oraz przycisk do wyjścia z programu.*



### Pasek postępu i komunikat o czasie

![odtwarzanie przekonwertowanego dźwięku w domyślnie ustawionym odtwarzaczu](images/odtwarzacz.png)
*Widok po wygenerowaniu pliku audio – automatyczne otwarcie domyślnego odtwarzacza po zakończeniu konwersji.*



![Widok GUI w trakcie przetwarzania teksty na mowę](images/w_trakcie.png)
*Interfejs podczas działania konwersji: aktywny pasek postępu oraz komunikat o przewidywanym czasie generowania audio.*



### Pasek postępu i komunikat o czasie

![Widok po zakończeniu przetwarzania](images/po_zakonczeniu.png)
*Ekran po zakończeniu konwersji: zapełniony pasek postępu oraz komunikat informujący o pomyślnym zakończeniu procesu.*



---

## Funkcjonalności aplikacji

- Wprowadzanie tekstu do konwersji.
- Wybór głosu i języka (PL/EN).
- Generowanie pliku MP3 z neuralnym TTS.
- Pasek postępu aktualizowany w czasie rzeczywistym.
- Informacja o przewidywanym czasie trwania operacji.
- Automatyczne odtwarzanie wygenerowanego pliku.
- Interfejs w stylu *superhero* (ttkbootstrap).

---

## Struktura projektu

- `main.py` – logika aplikacji i GUI  
- `edge_tts` – biblioteka odpowiedzialna za syntezę mowy  
- `threading` – wykonywanie TTS w tle  
- `asyncio` – obsługa asynchronicznego zapisu pliku  

---

## Uruchomienie

Instalacja zależności:

```bash
pip install edge-tts ttkbootstrap
```

Uruchomienie aplikacji:

```bash
python main.py
```

---

## Możliwe ulepszenia

- dodanie większej ilości głosu / języków do wyboru,
- możliwość wyboru lokalizacji zapisu,
- dodanie suwaka prędkości i wysokości głosu,
- tryb ciemny/jasny przełączany w GUI.

