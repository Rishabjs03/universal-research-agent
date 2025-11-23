from fastapi import APIRouter

from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.agents import build_agent
import os
from dotenv import load_dotenv


load_dotenv()


if not os.getenv("OPENAI_API_KEY") or not os.getenv("TAVILY_API_KEY"):
    raise Exception("Please set OPENAI_API_KEY and TAVILY_API_KEY in .env file")

router = APIRouter()

agent= build_agent()

class Query(BaseModel):
    input:str

@router.post("/ask")
def ask(query:Query):
    try:
        result = agent.invoke({"input":query.input})

        out = (
            result.get("output")
            or result.get("output_text")
            or result.get("result")
        )

        return{"response":out}

    except Exception as e:
        return{"error":str(e)}

