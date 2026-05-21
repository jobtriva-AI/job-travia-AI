<<<<<<< HEAD
import streamlit as st
import pdfplumber

from sklearn.metrics.pairwise import cosine_similarity

st.title("AI Recruitment Matcher")


uploaded_file = st.file_uploader("Upload Resume (PDF)")
job_description = st.text_area("Paste Job Description Here")

if uploaded_file and job_description:
    resume_text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                resume_text += text

   
  
    st.subheader(f"Match Score: {score}%")

    if score > 75:
        st.success("Strong Match")
    elif score > 50:
        st.warning("Moderate Match")
    else:
=======
import streamlit as st
import pdfplumber

from sklearn.metrics.pairwise import cosine_similarity

st.title("AI Recruitment Matcher")



uploaded_file = st.file_uploader("Upload Resume (PDF)")
job_description = st.text_area("Paste Job Description Here")

if uploaded_file and job_description:
    resume_text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                resume_text += text

    
    

    st.subheader(f"Match Score: {score}%")

    if score > 75:
        st.success("Strong Match")
    elif score > 50:
        st.warning("Moderate Match")
    else:
>>>>>>> 7e92a882a2b4f8e4818fe28022f40a8c63b2b697
        st.error("Low Match")
