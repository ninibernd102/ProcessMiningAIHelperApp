import streamlit as st
import os

FEEDBACK_LOG_FILE = "feedback_log.txt"

def log_feedback(user_input, assistant_response, feedback):
    """
    Loggt das Feedback des Nutzers in eine Datei.

    :param user_input: Eingabe des Nutzers
    :param assistant_response: Antwort der KI
    :param feedback: Feedback (Daumen hoch/runter)
    """
    log_entry = f"User Input: {user_input}\nAssistant Response: {assistant_response}\nFeedback: {feedback}\n{'-' * 40}\n"

    with open(FEEDBACK_LOG_FILE, "a", encoding="utf-8") as file:
        file.write(log_entry)

def render_feedback_section(user_input, assistant_response):
    """
    Rendert die Daumen hoch/runter-Schaltflächen für das Feedback.

    :param user_input: Eingabe des Nutzers
    :param assistant_response: Antwort der KI
    """
    st.markdown("### Wie zufrieden sind Sie mit der Antwort?")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("👍 Zufrieden"):
            log_feedback(user_input, assistant_response, "Daumen hoch")
            st.success("Ihr Feedback wurde gespeichert: 👍")

    with col2:
        if st.button("👎 Unzufrieden"):
            log_feedback(user_input, assistant_response, "Daumen runter")
            st.error("Ihr Feedback wurde gespeichert: 👎")