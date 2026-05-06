import os
from google.genai import types

MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash")

AGENT_NAME = "time_agent"
AGENT_DESCRIPTION = "Tells the current time in a specified city."
AGENT_INSTRUCTION = (
    "You are a helpful assistant that tells the current time in cities. "
    "Use the 'get_current_time' tool for this purpose."
)

CITY_TIMEZONES = {
    "dhaka": "Asia/Dhaka",
    "chittagong": "Asia/Dhaka",
    "chattogram": "Asia/Dhaka",
}

RETRY_OPTIONS = types.HttpRetryOptions(
    attempts=5,
    initial_delay=1.0,
    exp_base=2.0,
    max_delay=16.0,
    jitter=0.3,
    http_status_codes=[429, 500, 503, 504],
)

SUPPORTED_CITIES = list(CITY_TIMEZONES.keys())