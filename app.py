import streamlit as st
import pdfplumber
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime

# ---------------- LOGIN (SIMPLE) ----------------
def login():
    st.sidebar.title("🔐 Recruiter Login")

    user = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if user == "admin" and password == "admin123":
        st.sidebar.success("Login successful")
        return True
    elif user or password:
        st.sidebar.error("Invalid credentials")
    return False


# ---------------- APP CONFIG ----------------
st.set_page_config(page_title="Job Triva ATS", layout="wide")

st.title("📊 Job Triva ATS - Recruitment System")
st.caption("AI-powered Resume Screening & Ranking Tool")

# ---------------- AUTH ----------------
if not login():
    st.stop()

st.divider()

# ---------------- INPUT ----------------
job_description = st.text_area("📌 Paste Job Description", height=200)

uploaded_files = st.file_uploader(
    "📁 Upload Candidate Resumes (PDF)",
    type=["pdf"],
    accept_multiple_files=True
)

# ---------------- PDF TEXT EXTRACTION ----------------
def extract_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()
    return text

# ---------------- PROCESS ----------------
if uploaded_files and job_description:

    resumes = []
    names = []

    for file in uploaded_files:
        resumes.append(extract_text(file))
        names.append(file.name)

    # TF-IDF similarity (lightweight AI scoring)
    docs = resumes + [job_description]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(docs)

    scores = cosine_similarity(vectors[:-1], vectors[-1]).flatten()

    # Create dataframe
    df = pd.DataFrame({
        "Candidate": names,
        "Match Score (%)": (scores * 100).round(2)
    })

    # Ranking
    df = df.sort_values(by="Match Score (%)", ascending=False)

    st.subheader("🏆 Candidate Ranking")
    st.dataframe(df, use_container_width=True)

    # Status
    def status(score):
        if score >= 70:
            return "🟢 Strong Match"
        elif score >= 40:
            return "🟡 Moderate Match"
        else:
            return "🔴 Weak Match"

    df["Status"] = df["Match Score (%)"].apply(status)

    st.subheader("📊 Detailed Results")
    st.dataframe(df, use_container_width=True)

    # ---------------- DOWNLOAD ----------------
    excel_file = "shortlisted_candidates.xlsx"
    df.to_excel(excel_file, index=False)

    with open(excel_file, "rb") as f:
        st.download_button(
            "⬇️ Download Excel Report",
            f,
            file_name="Job_Triva_Candidates.xlsx"
        )

    st.success(f"Processed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

elif uploaded_files:
    st.warning("Please add job description")

elif job_description:
    st.warning("Please upload resumes")

else:
    st.info("Start by adding job description and uploading resumes")
