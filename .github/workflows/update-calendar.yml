import os
import requests
import hashlib

url = os.environ.get("ICS_URL")
token = os.environ.get("TELEGRAM_TOKEN")
chat_id = os.environ.get("TELEGRAM_CHAT_ID")

if not url:
    raise ValueError("ICS_URL non trovato nelle variabili ambiente.")

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=30)
response.raise_for_status()

content_type = response.headers.get("Content-Type", "")
content = response.content

if not content:
    raise ValueError("File ICS vuoto.")

new_hash = hashlib.md5(content).hexdigest()
old_hash = None

if os.path.exists("calendar.ics"):
    with open("calendar.ics", "rb") as f:
        old_hash = hashlib.md5(f.read()).hexdigest()

if old_hash and new_hash != old_hash:
    if token and chat_id:
        message = "⚠️ Il calendario è stato aggiornato!"
        telegram_response = requests.get(
            f"https://api.telegram.org/bot{token}/sendMessage",
            params={"chat_id": chat_id, "text": message},
            timeout=30
        )
        telegram_response.raise_for_status()
        print("Notifica Telegram inviata.")
    else:
        print("Calendario cambiato, ma TELEGRAM_TOKEN o TELEGRAM_CHAT_ID mancanti.")

with open("calendar.ics", "wb") as f:
    f.write(content)

print("calendar.ics scaricato correttamente.")
print(f"Content-Type ricevuto: {content_type}")
print(f"Dimensione file: {len(content)} bytes")
print(f"Nuovo hash: {new_hash}")
print(f"Vecchio hash: {old_hash}")
