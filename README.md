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
cd Projekt_Python_Scraping
docker-compose up --build
```
