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
    runner = InMemoryRunner(agent=root_agent)

    print("✅ Runner created.")

    query = "What is the time in Chittagong?"
    events = await call_llm(runner, query)

    print("Answer:")
    for event in events:
        if event.is_final_response() and event.content and event.content.parts:
            for part in event.content.parts:
                if getattr(part, "text", None):
                    print(part.text)


if __name__ == "__main__":
    asyncio.run(main())
