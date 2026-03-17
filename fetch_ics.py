import os
import requests

url = os.environ.get("ICS_URL")

if not url:
    raise ValueError("ICS_URL non trovato nelle variabili ambiente.")

response = requests.get(url, timeout=30)
response.raise_for_status()

content_type = response.headers.get("Content-Type", "")
content = response.content

if not content:
    raise ValueError("File ICS vuoto.")

with open("calendar.ics", "wb") as f:
    f.write(content)

print("calendar.ics scaricato correttamente.")
print(f"Content-Type ricevuto: {content_type}")
print(f"Dimensione file: {len(content)} bytes")
