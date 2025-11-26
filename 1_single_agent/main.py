import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from agent.agent import root_agent
from google.adk.runners import InMemoryRunner


load_dotenv()  
import asyncio

async def call_llm(runner, query):
    return await runner.run_debug(
        query
    )

async def main():
    # google_api_key = os.getenv("GOOGLE_API_KEY")
    # print("Google API Key:", google_api_key)
    # print(root_agent)
    runner = InMemoryRunner(agent=root_agent)

    print("✅ Runner created.")

    query = "What is the time in Chittagong?"
    response = await call_llm(runner, query)

    print(response)


if __name__ == "__main__":
    asyncio.run(main())
