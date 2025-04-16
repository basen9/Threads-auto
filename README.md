# Threads Followers Auto Tracker

Automatyczny system do śledzenia liczby obserwujących na Threads — aktualizowany co 4h w Airtable.

## Funkcje:
- Pobiera followersów z Threads (np. @zuck, @mosseri)
- Zapisuje do Airtable
- Pokazuje różnicę w ciągu 24h

## Wymagania:
- Airtable (token, base ID, table name)
- Render (jako Background Worker)
- Python 3.11+

## Pliki:
- `main.py` — główny skrypt
- `requirements.txt` — zależności
- `Dockerfile` — uruchamianie na Render.com

## Autor:
[@basen9](https://github.com/basen9)
