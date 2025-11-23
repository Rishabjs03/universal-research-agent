from fastapi import APIRouter,UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.agents import build_agent
from openai import OpenAI
import os
import base64
from dotenv import load_dotenv
import tempfile

load_dotenv()

client=OpenAI()
agent= build_agent()

router = APIRouter()


class VoiceResponse(BaseModel):
    user_text:str
    agent_text:str
    agent_audio:str

@router.post("/voice")
async def voice(audio: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False,suffix=".wav") as temp:
        temp.write(audio.file.read())
        temp_path=temp.name

    with open(temp_path,"rb") as f:
        transcription=client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            language="en"
        )

    user_text = transcription.text

    result= agent.invoke({"input":user_text})

    agent_text=(
        result.get("output")
        or result.get("output_text")
        or result.get("result")
    )

    tts=client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=agent_text
    )

    with tempfile.NamedTemporaryFile(delete=False,suffix=".mp3") as out:
        tts.stream_to_file(out.name)
        audio_bytes=open(out.name,"rb").read()
        audio_b64=base64.b64encode(audio_bytes).decode()
        mp3_path = out.name

    os.remove(temp_path)
    os.remove(mp3_path)

    return{
        "user_text":user_text,
        "agent_text":agent_text,
        "agent_audio":audio_b64
    }