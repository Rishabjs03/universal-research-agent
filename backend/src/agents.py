from langchain_openai import ChatOpenAI
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from src.tools import get_all_tool

def build_agent():
    tools = get_all_tool()
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    prompt = ChatPromptTemplate.from_messages([
        (
    "system",
    "You are a concise, speech-friendly AI research assistant. Always answer in short, simple, clear sentences that are easy to speak aloud. \
     Avoid long paragraphs. Avoid unnecessary details. \
    If the user asks for research, give the result in 3–5 bullet points. \
    If using tools, extract only essential facts. \
    Never include code blocks in final answers. \
    Never generate long essays. \
    Speak naturally, like a human explaining things. \
    Your answers will be converted to speech, so keep them concise and conversational."
    ),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)

    agent_executor = AgentExecutor(agent=agent,tools=tools,verbose=False)

    return agent_executor