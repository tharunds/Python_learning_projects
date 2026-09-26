import streamlit as st
from google import genai
from pypdf import PdfReader

# 1. Setup the Webpage Layout
st.set_page_config(page_title="AI Resume Matcher", page_icon="🎯", layout="wide")
st.title("🎯 AI Resume & Job Description Matcher")
st.write("Upload a PDF resume and paste a job description to analyze your ATS match.")

# 2. Safely connect to Google Gemini API
try:
    client = genai.Client()
except Exception:
    st.warning("⚠️ Configuration Alert: Make sure your GEMINI_API_KEY environment variable is set.")
    client = None

# 3. Create two columns for user inputs
col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Step 1: Upload Resume")
    uploaded_file = st.file_uploader("Choose your resume (PDF only)", type=["pdf"])

with col2:
    st.subheader("💼 Step 2: Paste Job Description")
    job_description = st.text_area("Paste the LinkedIn/corporate job description here...", height=200)

# 4. Trigger Analysis
if st.button("Run AI Analysis", type="primary"):
    if not client:
        st.error("API key is missing. Please set the GEMINI_API_KEY variable in your terminal.")
    elif uploaded_file is not None and job_description.strip() != "":
        with st.spinner("AI is evaluating your profile against the role..."):
            try:
                # Read and extract text from the PDF file
                reader = PdfReader(uploaded_file)
                resume_text = ""
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        resume_text += text
                
                # Instruct the AI on how to behave and format the response
                prompt = f"""
                You are an expert ATS (Applicant Tracking System) optimizer and HR manager.
                Analyze the following Resume against the Job Description provided.
                
                Provide the output strictly in the following format:
                ### 📊 Match Score
                [Give a realistic percentage match out of 100%, e.g., 78%]
                
                ### ❌ Missing Keywords & Skills
                [List bullet points of crucial skills or keywords present in the Job Description but missing/weak in the Resume]
                
                ### 💡 Actionable Improvement Steps
                [Provide 3 concise, specific tips on how to rewrite or update the resume to better align with the role]
                
                ---
                **RESUME:**
                {resume_text}
                
                **JOB DESCRIPTION:**
                {job_description}
                """
                
                # Send the request to Gemini 2.5 Flash
                response = client.models.generate_content(
                    model='gemini-3.8-flash',
                    contents=prompt,
                )
                
                # Show results on the web app screen
                st.success("Analysis Complete!")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.error("Please provide both a PDF resume and a job description to continue.")
