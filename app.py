import streamlit as st
import pdfplumber
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# PAGE TITLE
st.set_page_config(page_title="Job Triva AI Recruiter")

st.title("🚀 Job Triva AI Recruitment System")
st.write("Upload a resume and compare it with the job description.")

# JOB DESCRIPTION INPUT
job_description = st.text_area(
    "Enter Job Description",
    height=200,
    placeholder="Paste Reliance job description here..."
)

# RESUME UPLOAD
uploaded_file = st.file_uploader(
    "Upload Candidate Resume (PDF)",
    type=["pdf"]
)

# FUNCTION TO EXTRACT TEXT FROM PDF
def extract_text_from_pdf(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted

    return text

# MAIN LOGIC
if uploaded_file and job_description:

    resume_text = extract_text_from_pdf(uploaded_file)

    documents = [resume_text, job_description]

    cv = CountVectorizer().fit_transform(documents)

    similarity_score = cosine_similarity(cv)[0][1]

    match_percentage = round(similarity_score * 100, 2)

    st.subheader("📊 Matching Result")

    st.success(f"Candidate Match Score: {match_percentage}%")

    # SIMPLE DECISION
    if match_percentage >= 60:
        st.write("✅ Good Match for Reliance Job Role")
    else:
        st.write("❌ Candidate does not strongly match the role")

    # SHOW EXTRACTED RESUME TEXT
    with st.expander("View Extracted Resume Text"):
        st.write(resume_text)
