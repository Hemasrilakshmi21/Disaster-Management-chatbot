# app.py
# pip install streamlit google-genai

import streamlit as st
from google import genai

# ---------------------------
# API Key (IN CODE)
# ---------------------------
API_KEY = "AIzaSyCC8b2bCSdEVZYbBpPGIUqcnuJqU2lrjk4"  # rotate this later

client = genai.Client(api_key=API_KEY)

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Disaster Management Explainer Bot",
    page_icon="🆘",
    layout="centered"
)

st.title("🆘 Disaster Management Response & Relief Explainer Bot")

st.markdown("""
This bot explains **disaster response procedures, evacuation workflows,
and relief distribution processes**.

⚠️ Educational use only — not for real-time emergencies.
""")

# ---------------------------
# System Prompt
# ---------------------------
SYSTEM_PROMPT = """
You are a Disaster Management Response & Relief Process Explainer Bot.

Rules:
- Educational explanations only
- No predictions
- No emergency instructions
- No coordination or alerts
"""

# ---------------------------
# Session State
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------
# User Input
# ---------------------------
user_input = st.chat_input("Ask about disaster response or relief processes...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("assistant"):
        with st.spinner("Explaining..."):
            response = client.models.generate_content(
                model="gemini-3-flash-preview",   # ✅ FIX IS HERE
                contents=SYSTEM_PROMPT + "\n\nUser Question: " + user_input
            )

            reply = response.text
            st.markdown(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

# ---------------------------
# Footer
# ---------------------------
st.markdown("""
---
**Project:** Disaster Management Response & Relief Explainer Bot  
**Tech:** Gemini Flash Preview · Streamlit · Python
""")
