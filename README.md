# 🌍 Web Scraper Project (Distributed System)

System do pobierania i analizy danych ze stron internetowych, działający w architekturze rozproszonej.

---

## 📖 Opis projektu

Aplikacja umożliwia użytkownikowi wprowadzenie adresów URL poprzez interfejs webowy.  
Podane strony są następnie asynchronicznie pobierane i przetwarzane przez silnik scrapujący.  
Wyodrębnione dane (np. linki, emaile, numery telefonów) zapisywane są w bazie danych MongoDB.

---

## 🧩 Architektura systemu

Projekt składa się z trzech modułów:

- 🖥 **Interface (Flask + HTML/CSS)** – formularz do wprowadzania URL  
- 🔄 **Engine (asyncio + multiprocessing)** – równoległe scrapowanie stron  
- 🗃 **MongoDB** – przechowywanie danych  

📦 Całość działa w kontenerach Docker (Docker Compose)

---

## 🛠 Technologie

- Python 3 (Flask, aiohttp, BeautifulSoup, multiprocessing)  
- HTML / CSS  
- MongoDB  
- Docker + Docker Compose  

---

## ▶️ Uruchomienie

```bash
git clone https://github.com/rzepeeek/Projekt_Python_Scraping.git
cd Projekt_Python_Scraping/WEB-SCRAPER-PROJECT
docker-compose up --build
```

🌐 Aplikacja dostępna pod:
http://localhost:5000

---

## 📝 Instrukcja użycia

1. Wprowadź jeden lub więcej adresów URL  
2. Kliknij **Start**  
3. Aplikacja rozpocznie scrapowanie danych  
4. Wyniki zostaną zapisane w bazie MongoDB  

---

## 🔍 Testowanie

- Testy przeprowadzono lokalnie (Windows + Docker Desktop)  
- Poprawność zapisu danych zweryfikowano przy użyciu MongoDB Compass oraz mongosh  
- System poprawnie obsługuje wiele adresów URL i przetwarza je równolegle  

---

## 🚧 Dalszy rozwój

- 📊 Wyświetlanie wyników bezpośrednio w interfejsie webowym  
- ⏱ Automatyczne scrapowanie (harmonogram / scheduler)  
- 📬 Kolejka zadań (np. Redis + Celery)  
- 🎨 Ulepszenie interfejsu użytkownika  

---

## 👨‍💻 Autorzy

* Adrian Czarnota 21442
* Dawid Rzepka 21299

## 🔗 Repozytorium
https://github.com/rzepeeek/Projekt_Python_Scraping/tree/main/WEB-SCRAPER-PROJECT

---

