import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from agents.root_agent import root_agent
from services.runner import AgentRunner

load_dotenv()


async def main():
    runner = AgentRunner(root_agent)

    query = "What is the time in Chittagong?"
    events = await runner.run(query)

    response = AgentRunner.extract_response(events)
    if response:
        print(response)


if __name__ == "__main__":
    asyncio.run(main())