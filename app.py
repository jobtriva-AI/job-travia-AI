import streamlit as st

st.title("Job Triva AI Recruiter")

st.write("Upload resumes and match with job description")

job = st.text_area("Enter Job Description")

file = st.file_uploader("Upload Resume PDF", type=["pdf"])

if file:
    st.success("Resume uploaded successfully 🚀")

if job:
    st.info("Job description added")
