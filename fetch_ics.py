import os
import requests

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

content = response.content

if not content:
    raise ValueError("File ICS vuoto.")

with open("calendar.ics", "wb") as f:
    f.write(content)

if token and chat_id:
    telegram_response = requests.get(
        f"https://api.telegram.org/bot{token}/sendMessage",
        params={"chat_id": chat_id, "text": "✅ Test notifica GitHub riuscito"},
        timeout=30
    )
    telegram_response.raise_for_status()
    print("Notifica Telegram inviata.")
else:
    print("TELEGRAM_TOKEN o TELEGRAM_CHAT_ID mancanti.")

print("calendar.ics aggiornato.")
