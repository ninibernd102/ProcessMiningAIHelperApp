import streamlit as st
import pandas as pd
from utils import query_ollama

st.title("Process Mining Helper App")
st.write("Lade eine CSV-Datei hoch und stelle Fragen zur Auswahl eines Process-Mining-Algorithmus.")

# CSV-Upload
uploaded_file = st.file_uploader("Lade eine CSV-Datei hoch", type=["csv"])
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Vorschau der hochgeladenen Daten:", data.head())

# Frage an die KI
question = st.text_input("Frage an die KI:")
if question:
    st.write("KI wird befragt...")
    answer = query_ollama(question)
    st.write("Antwort der KI:", answer)
