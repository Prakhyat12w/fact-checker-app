import re
from typing import List, Dict


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def is_valid_claim(claim: str) -> bool:
    patterns = [
        r"\d",
        r"\b(USD|INR|EUR|dollars?|rupees?|percent|%)\b",
        r"\b(19|20)\d{2}\b"
    ]
    return any(re.search(p, claim, re.IGNORECASE) for p in patterns)


def deduplicate_claims(claims: List[str]) -> List[str]:
    seen = set()
    unique_claims = []
    for claim in claims:
        normalized = claim.lower().strip()
        if normalized not in seen:
            seen.add(normalized)
            unique_claims.append(claim)
    return unique_claims


def format_evidence(results: List[Dict]) -> str:
    formatted = []
    for r in results:
        title = r.get("title", "")
        url = r.get("url", "")
        content = r.get("content", "")
        formatted.append(f"- {title}\n  {url}\n  {content}")
    return "\n".join(formatted)
