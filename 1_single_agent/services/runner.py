import logging
from google.adk.runners import InMemoryRunner

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AgentRunner:
    def __init__(self, agent):
        self.runner = InMemoryRunner(agent=agent)
        logger.info("Runner created.")

    async def run(self, query: str):
        logger.info(f"Query: {query}")
        return await self.runner.run_debug(query)

    @staticmethod
    def extract_response(events):
        for event in events:
            if event.is_final_response() and event.content and event.content.parts:
                for part in event.content.parts:
                    if getattr(part, "text", None):
                        return part.text
        return None