import os
from dotenv import load_dotenv
from tavily import TavilyClient

# Load environment variables from a .env file
load_dotenv()

# Initialize the Tavily client
client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def tavily_search(query):
    response = client.search(
        query=query,
        max_results=5
    )

    results = []

    for i, r in enumerate(response["results"], 1):
        title = r.get("title", "Unknown")
        url = r.get("url", "")
        snippet = r.get("content", "").strip()
        
        # Cleanly truncate the snippet at a word boundary if it exceeds 300 characters
        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."
            
        results.append(f"{i}. **{title}**\n{url}\n{snippet}")
        
    return "\n\n".join(results)

    