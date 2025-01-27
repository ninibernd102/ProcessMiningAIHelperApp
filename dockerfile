# Basis-Image: Verwende ein schlankes Python-Image
FROM python:3.9-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Anforderungen in den Container
COPY requirements.txt .

# Installiere die Python-Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den restlichen Code ins Arbeitsverzeichnis
COPY . .

# Exponiere den Port für Streamlit
EXPOSE 8501

# Starte die Streamlit-App
CMD ["streamlit", "run", "app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
