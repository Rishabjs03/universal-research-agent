
# 🌐 Universal Research Agent + Voice Mode + Image Generation

An advanced multi-tool AI agent capable of Web Search, Data Analysis, Image Generation, and Real-Time Voice Interaction with interruption capabilities.

Powered by *LangChain*, *OpenAI GPT-4o*, *Tavily*, *Whisper*, and *Pygame*.

## 🚀 Features

**🔥 Research Agent (Text Mode)**
- 🔍 Web Search: Uses Tavily API for accurate, real-time information.

- 🌐 URL Reading: Can scrape and summarize specific web pages.

- 🧮 Python REPL: Writes and executes Python code for complex math & data logic.

- 🧠 Autonomous Reasoning: Uses a "Reason → Act → Observe" loop to solve multi-step problems.

**🎙️ Voice Agent (Jarvis Mode)**
- 🗣️ Real-Time Conversation: Powered by OpenAI Whisper (STT) and GPT-4o-mini-TTS.

- 🎧 Smooth Playback: Uses pygame for seamless audio handling.

- 🧠 Hands-Free: Full voice-controlled research assistant.


**🖼️ Image Generation**
- 🎨 AI Creativity: Integrated DALL-E 3 support.

- 👁️ Auto-Display: Generates and automatically opens images on your screen.
## 🏗️ Project Structure

```bash
universal-research-agent/
│
├── main.py               # 🖥️ Text-mode terminal agent
├── voice_agent.py        # 🎙️ Voice-enabled (Jarvis) agent
│
└── src/
    ├── agent.py          # 🧠 LLM + tool-calling logic
    └── tools.py          # 🛠️ Search, Python REPL, URL fetcher, Image Gen
│
├── .env.example          # 🔑 Environment variable template
├── requirements.txt      # 📦 Project dependencies
└── README.md             # 📄 Documentation

```
## 🔧 Setup

**1️⃣ Clone the Repository**
```bash
git clone https://github.com/Rishabjs03/universal-research-agent.git
cd universal-research-agent
```
**2️⃣ Create Virtual Environment**

 *macOS / Linux:*

```bash
python -m venv .venv
source .venv/bin/activate
```
*Windows:*

```bash
python -m venv .venv
.venv\Scripts\activate
```

**3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

**4️⃣ Configure Environment Variables**

*Create a .env file in the root directory and add your API keys:*

```bash
# Create .env file
cp .env.example .env
```

*Add your keys inside .env:*
```bash
OPENAI_API_KEY=sk-your-openai-key
TAVILY_API_KEY=tvly-your-tavily-key
```


## ▶️ Usage

**🖥️ Run Text Mode (Terminal Agent)**

- Best for coding, debugging, and silent research.

```bash
python main.py
```

**🎙️ Run Voice Mode (Jarvis Agent)**

- Best for hands-free interaction. Headphones recommended to prevent audio feedback loops.

```bash
python voice_agent.py
```


## 🧠 Tech Stack

- **LLM:** OpenAI GPT-4o / GPT-4o-mini

- **Framework:** LangChain (Agents & Tools)

- **Search:** Tavily API

- **Voice (STT):** OpenAI Whisper-1

- **Voice (TTS):** OpenAI TTS-1

- **Audio Engine:** Pygame (for interruptible playback)

- **Vision/Image:** DALL-E 3 & OpenCV



## License

This project is licensed under the MIT License – free to use, modify, and distribute.
## Support

**if you find this project useful, please give it a Star ⭐ on GitHub!**

- 🐛 **Report Issues:** Issues Tab

- 🤝 **Contribute:** Pull requests are welcome!

