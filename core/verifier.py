from tavily import TavilyClient
import os

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def verify_claim(claim):
    search = tavily.search(query=claim, max_results=5)
    return search.get("results", [])
