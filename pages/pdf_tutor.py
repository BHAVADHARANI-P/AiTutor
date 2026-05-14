import streamlit as st
from utils.pdf_reader import read_pdf
from utils.ai_response import get_ai_response

st.title("📘 PDF Tutor")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:

    text = read_pdf(uploaded_file)

    st.success("PDF Uploaded Successfully")

    if st.button("Summarize PDF"):

        prompt = f"Summarize this content:\n{text}"

        summary = get_ai_response(prompt)

        st.write(summary)
