import streamlit as st
from utils.quiz_generator import generate_quiz

st.title("📝 AI Quiz Generator")

topic = st.text_input("Enter Topic")

if st.button("Generate Quiz"):

    quiz = generate_quiz(topic)

    st.write(quiz)
