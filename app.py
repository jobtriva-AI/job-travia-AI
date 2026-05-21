import streamlit as st

st.set_page_config(page_title="Job Triva ATS", layout="wide")

st.title("📊 Job Triva ATS")

st.success("App is running successfully 🚀")

st.write("If you see this, Streamlit is working correctly.")

job = st.text_area("Job Description")

file = st.file_uploader("Upload Resume PDF")

if file:
    st.info("File uploaded successfully")

if job:
    st.info("Job description added")
