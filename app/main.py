import streamlit as st
from ui import render_ui

st.set_page_config(layout="wide")

def main():
    st.title("Process Mining Helper App")
    st.write("Lade eine CSV-Datei hoch und stelle Fragen zur Auswahl eines Process-Mining-Algorithmus.")

    # Rendern der UI
    render_ui()

if __name__ == "__main__":
    main()