import streamlit as st
import pdfplumber

st.title("Job Triva AI Recruiter")

st.write("Upload resume and compare with job description")

job = st.text_area("Job Description")

file = st.file_uploader("Upload PDF Resume", type=["pdf"])

def extract(pdf):
    text = ""
    with pdfplumber.open(pdf) as f:
        for p in f.pages:
            if p.extract_text():
                text += p.extract_text()
    return text

if file and job:
    resume = extract(file)

    st.subheader("Resume Text")
    st.write(resume)

    st.subheader("Job Text")
    st.write(job)

    if len(resume) > 0:
        match = min(100, len(resume) / len(job) * 100)
        st.success(f"Basic Match Score: {round(match,2)}%")
