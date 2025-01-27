# logic.py
import streamlit as st
from models import ProcessAttributes

def get_process_attributes():
    """
    Erstellt ein ProcessAttributes-Objekt basierend auf den Nutzereingaben.
    """
    attributes = ProcessAttributes()
    attributes.goal = st.session_state.get("goal", "")
    attributes.num_traces = st.session_state.get("num_traces", "")
    attributes.num_activities = st.session_state.get("num_activities", "")
    attributes.process_complexity = st.session_state.get("process_complexity", "")
    attributes.has_loops = st.session_state.get("has_loops", "")
    attributes.has_parallelism = st.session_state.get("has_parallelism", "")
    attributes.data_completeness = st.session_state.get("data_completeness", "")
    attributes.data_noise = st.session_state.get("data_noise", "")
    attributes.has_timestamps = st.session_state.get("has_timestamps", "")
    attributes.easy_interpretation = st.session_state.get("easy_interpretation", "")
    attributes.speed_importance = st.session_state.get("speed_importance", "")
    attributes.programming_language = st.session_state.get("programming_language", "")
    return attributes

def create_prompt(attributes):
    """
    Erstellt ein Prompt basierend auf den ProcessAttributes.
    """
    prompt = f"""
    Basierend auf den folgenden Informationen, empfehle den besten Process-Mining-Algorithmus:
    - Zielsetzung: {attributes.goal}
    - Anzahl der Spuren: {attributes.num_traces}
    - Anzahl der Aktivitäten: {attributes.num_activities}
    - Prozesskomplexität: {attributes.process_complexity}
    - Enthält Schleifen: {attributes.has_loops}
    - Enthält Parallelität: {attributes.has_parallelism}
    - Datenvollständigkeit: {attributes.data_completeness}
    - Datenrauschen: {attributes.data_noise}
    - Zeitstempel vorhanden: {attributes.has_timestamps}
    - Einfache Interpretation gewünscht: {attributes.easy_interpretation}
    - Geschwindigkeit wichtig: {attributes.speed_importance}
    - Programmiersprache: {attributes.programming_language}
    """
    return prompt