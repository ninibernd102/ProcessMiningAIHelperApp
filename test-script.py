import requests
import json

# URL und Header
url = "http://127.0.0.1:11434/api/chat"
headers = {"Content-Type": "application/json"}

# Daten für den POST-Request
data = {
    "model": "llama3.2",
    "messages": [
        {
            "role": "user",
            "content": "Was ist der Sinn des Lebens?"
        }
    ],
    "stream": False
}

# Anfrage senden
try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()  # Fehler bei ungültigem Statuscode
    print("Antwort von der KI:", response.json())
except requests.exceptions.RequestException as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
