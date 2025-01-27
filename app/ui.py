import streamlit as st
import pandas as pd
from connection import query_ollama
from logic import get_process_attributes, create_prompt
from config import DEFAULT_OPTIONS
from feedback import render_feedback_section

def render_ui():

    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    col1, col2 = st.columns([2, 3])

    with col1:
        st.header("Bitte geben Sie Informationen zu Ihrem Prozess an:")

        # 1. Zielsetzung
        st.subheader("Zielsetzung")
        st.session_state["goal"] = st.selectbox(
            "Was möchten Sie mit Process Mining erreichen?",
            options=["Bitte wählen"] + DEFAULT_OPTIONS["goal"]
        )

        # 2. Prozessmerkmale
        st.subheader("Prozessmerkmale")
        st.session_state["num_traces"] = st.selectbox(
            "Wie viele Prozessinstanzen (Spuren) haben Sie?",
            options=["Bitte wählen"] + DEFAULT_OPTIONS["num_traces"]
        )
        st.session_state["num_activities"] = st.selectbox(
            "Wie viele verschiedene Aktivitäten gibt es in Ihrem Prozess?",
            options=["Bitte wählen"] + DEFAULT_OPTIONS["num_activities"]
        )
        st.session_state["process_complexity"] = st.selectbox(
            "Wie komplex ist Ihr Prozess?",
            options=["Bitte wählen"] + DEFAULT_OPTIONS["process_complexity"]
        )
        st.session_state["has_loops"] = st.selectbox(
            "Enthält Ihr Prozess Schleifen (wiederholte Aktivitäten)?",
            options=["Bitte wählen"] + DEFAULT_OPTIONS["has_loops"]
        )
        st.session_state["has_parallelism"] = st.selectbox(
            "Enthält Ihr Prozess parallele Aktivitäten (gleichzeitige Ausführung)?",
            options=["Bitte wählen"] + DEFAULT_OPTIONS["has_parallelism"]
        )

        # 3. Datenqualität
        st.subheader("Datenqualität")
        st.session_state["data_completeness"] = st.selectbox(
            "Sind Ihre Daten vollständig (fehlen keine wichtigen Informationen)?",
            options=["Bitte wählen"] + DEFAULT_OPTIONS["data_completeness"]
        )
        st.session_state["data_noise"] = st.selectbox(
            "Enthalten Ihre Daten Rauschen (fehlerhafte oder irrelevante Einträge)?",
            options=["Bitte wählen"] + DEFAULT_OPTIONS["data_noise"]
        )
        st.session_state["has_timestamps"] = st.selectbox(
            "Enthalten Ihre Daten Zeitstempel (Zeitpunkte für jede Aktivität)?",
            options=["Bitte wählen"] + DEFAULT_OPTIONS["has_timestamps"]
        )

        # 4. Benutzerfreundlichkeit
        st.subheader("Benutzerfreundlichkeit")
        st.session_state["easy_interpretation"] = st.selectbox(
            "Möchten Sie ein einfach zu interpretierendes Prozessmodell?",
            options=["Bitte wählen"] + DEFAULT_OPTIONS["easy_interpretation"]
        )
        st.session_state["speed_importance"] = st.selectbox(
            "Ist die Geschwindigkeit der Analyse wichtig für Sie?",
            options=["Bitte wählen"] + DEFAULT_OPTIONS["speed_importance"]
        )

        # 5. Technische Anforderungen
        st.subheader("Technische Anforderungen")
        st.session_state["programming_language"] = st.selectbox(
            "Müssen Sie den Algorithmus in einer bestimmten Programmiersprache implementieren?",
            options=["Bitte wählen"] + DEFAULT_OPTIONS["programming_language"]
        )

        if st.button("Algorithmusempfehlung anfordern"):
            attributes = get_process_attributes()
            prompt = create_prompt(attributes)
            st.write("KI wird befragt...")
            answer = query_ollama(prompt)
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            st.session_state.chat_history.append({"role": "assistant", "content": answer})

            st.markdown("### Antwort der KI:")
            st.write(answer)
            render_feedback_section(prompt, answer)

        uploaded_file = st.file_uploader("Lade eine CSV-Datei hoch", type=["csv"])
        if uploaded_file:
            data = pd.read_csv(uploaded_file)
            st.write("Vorschau der hochgeladenen Daten:", data.head())

    with col2:
        st.header("Chat mit der KI")
        user_input = st.text_input("Stelle eine Frage an die KI:")

        if user_input:
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            st.write("KI wird befragt...")
            answer = query_ollama(user_input, st.session_state.chat_history)
            st.session_state.chat_history.append({"role": "assistant", "content": answer})

            st.markdown("### Antwort der KI:")
            st.write(answer)
            render_feedback_section(user_input, answer)

        chat_pairs = []
        pair = {"user": None, "assistant": None}

        for message in st.session_state.chat_history:
            if message["role"] == "user":
                pair["user"] = message["content"]
            elif message["role"] == "assistant":
                pair["assistant"] = message["content"]
                chat_pairs.append(pair)
                pair = {"user": None, "assistant": None}

        for pair in chat_pairs:
            if pair["user"]:
                st.markdown(f"**Du:** {pair['user']}")
            if pair["assistant"]:
                st.markdown(f"**KI:** {pair['assistant']}")
            st.markdown("<hr style='margin:10px 0;'>", unsafe_allow_html=True)
