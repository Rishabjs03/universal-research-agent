from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_experimental.tools import PythonREPLTool
from langchain.tools import tool
from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO

# Web-search-tool
def get_search_tool():
    return TavilySearchResults(
        max_results=3,
        name="web_search",
        description="Search the web for current events, numbers, facts, and summaries."
    )

# Python-repl-tool
def get_python_repl_tool():

    return PythonREPLTool(
         name="python_repl",
        description="Run Python code to perform calculations and data processing."
    )

# URL-content-fetcher-tool
@tool
def fetch_url_content(url: str) -> str:
    """
    Fetch the HTML content of a URL and return the first 4000 characters.
    Helps the AI agent read articles or web pages directly.
    """
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        text = resp.text
        return text[:4000] + ("..." if len(text) > 4000 else "")
    except Exception as e:
        return f"Error reading URL: {e}"



@tool
def generate_image(prompt: str):
    """Use this tool to generate/create/draw an image based on a user's prompt."""
    client = OpenAI()

    try:
        # 1. Generate
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url

        # 2. Download and Show immediately
        img_response = requests.get(image_url)
        img = Image.open(BytesIO(img_response.content))
        img.show() # This opens the image viewer

        return f"I have generated the image of '{prompt}' and opened it on your screen."
    except Exception as e:
        return f"Error generating image: {e}"

# Sending all tools to the main executor
def get_all_tool():
    return [get_search_tool(), get_python_repl_tool(), fetch_url_content,generate_image]
