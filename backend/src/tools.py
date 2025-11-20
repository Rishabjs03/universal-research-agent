from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_experimental.tools import PythonREPLTool
from langchain.tools import tool
import requests

def get_search_tool():
    """Tavily search wrapper (web search for current facts)."""
    return TavilySearchResults(
        max_results=3,
        description="Search the web for current events, market data and facts."
    )

def get_python_repl_tool():
    """Python REPL wrapper (for quick code experiments)."""
    return PythonREPLTool()

@tool
def fetch_url_content(url: str) -> str:
    """
    Simple URL fetcher. Returns first chunk of text to save tokens.
    Keep this for reading pages given direct links.
    """
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        text = resp.text
        return text[:4000] + ("..." if len(text) > 4000 else "")
    except Exception as e:
        return f"Error reading URL: {e}"


def get_all_tool():
    return [get_search_tool(), get_python_repl_tool(), fetch_url_content]
