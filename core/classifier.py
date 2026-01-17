from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)


def classify_claim(claim, evidence):
    prompt = f"""
Claim: {claim}

Evidence:
{evidence}

Classify the claim as one of:
Verified, Inaccurate, or False.
Give a one-line justification.
"""
    response = llm.invoke(prompt)
    return response.content
