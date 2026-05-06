from datetime import datetime
from zoneinfo import ZoneInfo
from config.settings import CITY_TIMEZONES, SUPPORTED_CITIES


def get_current_time(city: str) -> dict:
    key = (city or "").strip().lower()
    tz_name = CITY_TIMEZONES.get(key)

    if not tz_name:
        return {
            "status": "error",
            "city": city,
            "error": f"Unsupported city. Try: {', '.join(city.title() for city in SUPPORTED_CITIES)}.",
        }

    now_local = datetime.now(ZoneInfo(tz_name))

    return {
        "status": "success",
        "city": city,
        "timezone": tz_name,
        "time": now_local.strftime("%I:%M %p"),
        "iso": now_local.isoformat(),
    }

