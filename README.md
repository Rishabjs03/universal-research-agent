#Universal-Research-Agent

A fully autonomous AI agent that can:

- 🔍 Search the web (Tavily)
- 📄 Read & analyze URLs
- 🧮 Run Python code for calculations
- 🧠 Use tool-calling LLM reasoning
- 🔁 Perform multi-step research loops

Built using:
- LangChain
- OpenAI models
- Tavily Search API

---

## 🚀 Features

- Multi-tool agent execution
- Search + URL reading + Python REPL
- Autonomous Reason → Act → Observe loop
- Modular tool system
- Terminal-based interface
- Works with GPT-4 and GPT-o models

---

## 🏗️ Project Structure

ai-multi-tool-agent/

├── main.py

└── src/

├── agent.py

└── tools.py

---

## 🔧 Setup

### 1. Clone Repo
git clone https://github.com/Rishabjs03/universal-research-agent.git
cd backend


### 2. Create Virtual Environment

python -m venv .venv
source .venv/bin/activate # mac/linux
..venv\Scripts\activate # windows


### 3. Install Dependencies

pip install -r requirements.txt


### 4. Configure Environment Variables

Copy `.env.example` → `.env` and add:
OPENAI_API_KEY=your-key
TAVILY_API_KEY=your-key


---

## ▶️ Run the Agent

python main.py


---

## 🧪 Example Prompts

-Search the current population of India, China and USA. Then use Python to calculate ratios.

-Search latest AI news from 48 hours and summarize the top 3 factual updates.

-Read this URL https://bbc.com/news/world-us-canada-67195422 and give a 5-point summary.


---

## 📜 License
MIT License – free to modify and use.

---

## ⭐ Support
Star the repo if you like this project!

