from langchain_groq import ChatGroq
from utils.prompts import CLAIM_EXTRACTION_PROMPT

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)


def extract_claims(text):
    response = llm.invoke(CLAIM_EXTRACTION_PROMPT + "\n\n" + text)
    claims = response.content.split("\n")
    return [c.strip("- ").strip() for c in claims if c.strip()]
