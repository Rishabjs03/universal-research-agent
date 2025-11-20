from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_experimental.tools import PythonREPLTool
from langchain.tools import tool
import requests

# Web-search-tool
def get_search_tool():

    return TavilySearchResults(
        max_results=3,
        description="Search the web for current events, market data and facts."
    )

# Python-repl-tool
def get_python_repl_tool():

    return PythonREPLTool()

# URL-content-fetcher-tool
@tool
def fetch_url_content(url: str) -> str:

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        text = resp.text
        return text[:4000] + ("..." if len(text) > 4000 else "")
    except Exception as e:
        return f"Error reading URL: {e}"

# Sending all tools to the main executor
def get_all_tool():
    return [get_search_tool(), get_python_repl_tool(), fetch_url_content]
