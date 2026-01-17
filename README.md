# AI Fact-Checking Web App

An AI-powered web application that extracts factual claims from uploaded PDF documents, verifies them against live web data, and classifies each claim as **Verified**, **Inaccurate**, or **False** with concise reasoning and sources.

This tool acts as a **fact-checking layer before publication**, helping identify outdated statistics, incorrect claims, and unsupported assertions in reports, articles, or research documents.

---

## 🚀 Features

- 📄 **PDF Upload** – Drag-and-drop interface for uploading documents
- 🧠 **Claim Extraction** – Identifies non-trivial, check-worthy factual claims
- 🌐 **Live Web Verification** – Cross-checks claims using real-time web search
- ✅ **Claim Classification**
  - Verified
  - Inaccurate (outdated or mismatched data)
  - False (no supporting evidence)
- 📊 **Clear Results Display** – Each claim shown with verdict and reasoning
- ☁️ **Fully Deployed** – Accessible via a public URL (Streamlit Cloud)

---

## 🏗️ Tech Stack

| Layer | Technology |
|------|-----------|
| Frontend | Streamlit |
| Backend | Python |
| LLM | Groq (LLaMA 3.1 – 8B Instant) |
| Orchestration | LangChain |
| Web Search | Tavily API |
| PDF Parsing | pdfplumber |
| Deployment | Streamlit Cloud |

---

## 🧠 How It Works

1. **Upload PDF**
   - User uploads a document via the web interface.

2. **Text Extraction**
   - Text is extracted from the PDF using `pdfplumber`.

3. **Claim Extraction**
   - An LLM extracts only **non-trivial, verifiable claims** (e.g., statistics, prices, events).
   - Obvious facts (dates, calendar truths, definitions) are intentionally ignored.

4. **Live Verification**
   - Each claim is searched on the live web using Tavily.
   - Relevant evidence is collected.

5. **Classification**
   - Claims are classified as **Verified**, **Inaccurate**, or **False**.
   - A short justification is generated for each verdict.

6. **Results Display**
   - Claims and verdicts are displayed clearly in the UI.

---

## 📁 Project Structure

fact-checker-app/
│
├── app.py # Streamlit entry point
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules
│
├── core/
│ ├── pdf_loader.py # PDF text extraction
│ ├── claim_extractor.py # Claim identification logic
│ ├── verifier.py # Web verification via Tavily
│ └── classifier.py # Claim classification logic
│
├── utils/
│ ├── prompts.py # LLM prompt templates
│ └── helpers.py # Utility functions

## ⚙️ Setup & Installation (Local)

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/fact-checker-app.git
cd fact-checker-app
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```
### 3. Install Dependencies
pip install -r requirements.txt

### 4. Environment Variables

Create a .env file (do not commit this):

GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key

### 5. Run the App
streamlit run app.py


Open http://localhost:8501 in your browser.

### The app is deployed using Streamlit Cloud.

Deployment Steps

Push the code to GitHub (excluding .env)

Go to https://share.streamlit.io

Create a new app from the repository

Set app.py as the entry point

Add secrets in App Settings → Secrets:

GROQ_API_KEY = "gsk_..."
TAVILY_API_KEY = "tvly_..."


### 🎥 Demo

A short demo video demonstrates:

Uploading a PDF

Extracting claims

Flagging incorrect or outdated information

(Demo video link provided in submission)

### 📌 Evaluation Criteria Alignment

This project satisfies all required criteria:

✅ Live, deployed web app

✅ Extracts verifiable claims from PDFs

✅ Uses live web data for verification

✅ Flags false and outdated information

✅ Clean codebase with documentation

✅ Public URL for immediate testing

### 🔒 Security & Best Practices

API keys are never committed

.env is excluded via .gitignore

Secrets are injected securely at runtime

### 📜 License

This project is intended for educational and evaluation purposes.

### 🙌 Acknowledgements

Groq for fast, free LLM inference
Tavily for reliable real-time web search
Streamlit for rapid UI deployment
LangChain for orchestration
