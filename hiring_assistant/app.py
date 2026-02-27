import streamlit as st
from llm_handler import generate_response
from prompt import SYSTEM_PROMPT, tech_question_prompt

st.set_page_config(page_title="TalentScout Hiring Assistant")

st.title("🤖 TalentScout Hiring Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

# Greeting
if len(st.session_state.messages) == 1:
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hello! Welcome to TalentScout 🚀\nI will assist you with the initial screening. Let's begin.\nWhat is your Full Name?"
    })

for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your response...")

if user_input:
    if user_input.lower() in ["exit", "quit", "bye"]:
        st.chat_message("assistant").markdown(
            "Thank you for applying! Our team will contact you soon. 😊"
        )
        st.stop()

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    response = generate_response(st.session_state.messages)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.chat_message("assistant").markdown(response)
   