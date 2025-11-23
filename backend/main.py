
import os
from dotenv import load_dotenv
from src.agents import build_agent



load_dotenv()




# checking the api key
if not os.getenv("OPENAI_API_KEY") or not os.getenv("TAVILY_API_KEY"):
    print("Error: Please set OPENAI_API_KEY and TAVILY_API_KEY in .env file")
    exit(1)

# main executor function
def main():
    print("🤖 Multi-Tool Research Agent — ready.")
    print("Type 'exit' or CTRL+C to quit.")

    # calling the agent executor
    agent_executor = build_agent()

    while True:
        try:
            user_input= input("\nUser:").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit","quit","bye"]:
                break

            result = agent_executor.invoke({"input":user_input})
            print("\nAssistant:", result)

            out = None
            if isinstance(result, dict):
                out = result.get("output") or result.get("output_text") or result.get("result")
            else:
                out = str(result)
            print(f"\n🤖 Agent:\n{out}\n")
        except KeyboardInterrupt:
            print("\nExiting.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
