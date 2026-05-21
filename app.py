import streamlit as st

st.title("Job Triva AI Recruiter")

st.write("App is running successfully 🚀")

job = st.text_area("Job Description")
file = st.file_uploader("Upload Resume PDF")

if file:
    st.success("File uploaded successfully!")

if job:
    st.info("Job description received!")
