from datetime import datetime
from zoneinfo import ZoneInfo

from google.genai import types
from google.adk.agents.llm_agent import Agent

CITY_TO_TZ = {
    "dhaka": "Asia/Dhaka",
    "chittagong": "Asia/Dhaka",
    "chattogram": "Asia/Dhaka",
}

def get_current_time(city: str) -> dict:
    key = (city or "").strip().lower()
    tz_name = CITY_TO_TZ.get(key)
    if not tz_name:
        return {
            "status": "error",
            "city": city,
            "error": "Unsupported city. Try: Dhaka, Chittagong (Chattogram).",
        }

    now_local = datetime.now(ZoneInfo(tz_name))
    return {
        "status": "success",
        "city": city,
        "timezone": tz_name,
        "time": now_local.strftime("%I:%M %p"),
        "iso": now_local.isoformat(),
    }

retry_options = types.HttpRetryOptions(
    attempts=5,
    initial_delay=1.0,
    exp_base=2.0,
    max_delay=16.0,
    jitter=0.3,
    http_status_codes=[429, 500, 503, 504],
)

root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="Tells the current time in a specified city.",
    instruction=(
        "You are a helpful assistant that tells the current time in cities. "
        "Use the 'get_current_time' tool for this purpose."
    ),
    tools=[get_current_time],
    generate_content_config=types.GenerateContentConfig(
        http_options=types.HttpOptions(
            retry_options=retry_options
        )
    ),
)
