CLAIM_EXTRACTION_PROMPT = """
Extract ONLY non-trivial, check-worthy factual claims from the text.

STRICT RULES:
- Ignore obvious or self-evident facts (e.g., calendar dates, definitions, chronological truths).
- Ignore generic statements like "X is a year", "January is a month".
- ONLY extract claims involving:
- Numerical values (prices, percentages, counts)
- Time-bound real-world events
- Financial, economic, or market statistics
- Technical, scientific, or policy-related assertions
- Each claim must be something that could realistically be false, outdated, or misleading.

Return each claim as a bullet point.
"""
