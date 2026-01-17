from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH, override=True)

import streamlit as st
from core.pdf_loader import extract_text_from_pdf
from core.claim_extractor import extract_claims
from core.verifier import verify_claim
from core.classifier import classify_claim

st.set_page_config(page_title="AI Fact Checker", layout="wide")

st.title("📄 AI Fact-Checking Web App")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text..."):
        text = extract_text_from_pdf(uploaded_file)

    with st.spinner("Identifying claims..."):
        claims = extract_claims(text)

    st.subheader("Verification Results")

    for claim in claims:
        with st.expander(claim):
            evidence = verify_claim(claim)
            verdict = classify_claim(claim, evidence)
            st.write(verdict)
