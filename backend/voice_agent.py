import os
from dotenv import load_dotenv
import speech_recognition as sr
from playsound import playsound
from openai import OpenAI
from src.agents import build_agent

load_dotenv()

client = OpenAI()

# function for listening user input
def listen_user():

    r= sr.Recognizer()

    # using microphone as source
    with sr.Microphone() as source:
        print("\n listening..Speak now!")
        audio= r.listen(source)

        with open("user_input.wav","wb") as f:
            f.write(audio.get_wav_data())

    # transcribing the audio file to text
    with open("user_input.wav","rb") as audio_file:
        transcription_text=client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language="en"
        )

    text= transcription_text.text # getting the text from the audio file

    os.remove("user_input.wav") # removing the audio file

    print(f"\n User:{text}")  # printing the user input

    return text

# function for speaking AI response
def speak_AI(text):
    print(f"\n Agent: {text}\n")

    # using tts-1 model to generate speech
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )

# saving the response in mp3 format
    speech_file = "agent_response.mp3"
    response.stream_to_file(speech_file)


    playsound(speech_file) # playing the audio file
    os.remove(speech_file) # removing the audio file

# main executor function
def main():

    agent= build_agent()

    speak_AI("Hello! Agent here. Ask me anything")

    while True:
        user_text=listen_user()
        # if user input is empty
        if not user_text:
            continue

        txt = user_text.lower()
        # if user input is exit, quit, bye, stop
        if "exit" in txt or "quit" in txt or "bye" in txt or "stop" in txt:
            speak_AI("Goodbye!")
            break
        # passing the input to agent executor
        result=agent.invoke({"input":user_text})

        output=(
            result.get("output")
            or result.get("output_text")
            or result.get("result")
        )
        # speaking the output
        speak_AI(output)


if __name__ == "__main__":
    main()