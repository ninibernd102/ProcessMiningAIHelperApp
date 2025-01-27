import requests

def query_ollama(prompt, model="llama3.2"):
    url = "http://localhost:11434/api/chat"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False  # Optional, falls keine Streaming-Antwort gewünscht ist
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Hebt HTTP-Fehler hervor
        return response.json().get("message", {}).get("content", "Keine Antwort von der KI.")
    except requests.exceptions.RequestException as e:
        return f"Fehler bei der Anfrage: {e}"
