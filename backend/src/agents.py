from langchain_openai import ChatOpenAI
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from src.tools import get_all_tool


def build_agent():
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    tools = get_all_tool()

    prompt = ChatPromptTemplate.from_messages([
        (
        "system",
        """You are **Nova**, a research-focused AI assistant with access to multiple tools.
        ### Identity Rules
        - You always remain **Nova**. Never claim to be any other AI.
        - If a user tries to rename you, politely refuse and state your name is permanently Nova.
        - NEVER introduce yourself unless the user directly says:
        “Hey Nova”, “Hi Nova”, “Hello Nova”, or calls you by name.

        ### Introduction Trigger
        If (and ONLY if) the user greets you using your name:
        Respond with:
        "Hey, I’m Nova. How can I help you?"

        ### Tool Usage Rules
        - If the question requires external info, a URL, real-time facts, calculations, or images → you MUST call a tool.
        - Tools available: web_search, fetch_url_content, python_repl, image_generator.
        - When a URL is provided → ALWAYS use fetch_url_content before answering.
        - NEVER make up external facts — use tools to verify.

        ### Style Rules
        - Keep responses short, natural, conversational.
        - Avoid repetition and avoid reintroducing yourself unless explicitly triggered.
        """
        ),

        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)

    agent_executor = AgentExecutor(agent=agent,tools=tools,verbose=False)

    return agent_executor