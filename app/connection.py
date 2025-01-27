import requests
from config import KI_MODEL

def query_ollama(prompt, messages=[]):
    """
    Sendet ein Prompt zusammen mit dem Chat-Verlauf an die Ollama-KI und gibt die Antwort zurück.
    """
    url = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": KI_MODEL,
        "messages": messages + [{"role": "user", "content": prompt}],
        "stream": False  
    }

    try:
        # Senden der Anfrage
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  

        # Verarbeiten der Antwort
        response_json = response.json()
        message = response_json.get("message", {}).get("content", None)
        if not message:
            return "Die KI hat keine gültige Antwort zurückgegeben."
        return message
    except requests.exceptions.RequestException as e:
        return f"Fehler bei der Anfrage: {e}"
