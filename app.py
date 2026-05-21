import streamlit as st

st.title("Job Triva AI Recruitment System")

st.write("AI Recruitment System is running successfully 🚀")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded_file:
    st.success("Resume uploaded successfully!")
