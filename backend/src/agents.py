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
            "You are a helpful research assistant. You can search the web and run python code to answer questions."
        ),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)

    agent_executor = AgentExecutor(agent=agent,tools=tools,verbose=False)

    return agent_executor