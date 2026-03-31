import pdfplumber
import streamlit as st

st.header("My First Chatbot")

with st.sidebar:
    st.title("My First Chatbot")
    file = st.file_uploader("Please upload the pdf file and start asking questions", type=["pdf"])

if file is not None:
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:  # avoid None
                text += page_text + "\n\n"
    st.write(text)