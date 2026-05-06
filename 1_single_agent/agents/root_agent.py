from google.genai import types
from google.adk.agents.llm_agent import Agent
from config.settings import (
    MODEL_NAME,
    AGENT_NAME,
    AGENT_DESCRIPTION,
    AGENT_INSTRUCTION,
    RETRY_OPTIONS,
)
from tools.time_tools import get_current_time


root_agent = Agent(
    model=MODEL_NAME,
    name=AGENT_NAME,
    description=AGENT_DESCRIPTION,
    instruction=AGENT_INSTRUCTION,
    tools=[get_current_time],
    generate_content_config=types.GenerateContentConfig(
        http_options=types.HttpOptions(retry_options=RETRY_OPTIONS)
    ),
)