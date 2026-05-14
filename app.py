import streamlit as st
from utils.ai_response import get_ai_response

st.set_page_config(page_title="AI Tutor", layout="wide")

st.title("🎓 AI Tutor")

subject = st.selectbox(
    "Choose Subject",
    ["Programming", "Maths", "Physics", "ECE"]
)

question = st.text_area("Ask Your Question")

if st.button("Get Answer"):

    if question:
        prompt = f'''
        You are an AI tutor.
        Subject: {subject}

        Explain clearly and simply:
        {question}
        '''

        answer = get_ai_response(prompt)

        st.subheader("Answer")
        st.write(answer)

    else:
        st.warning("Please enter a question")
