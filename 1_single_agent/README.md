# Single Agent

A simple AI agent that tells the current time in Bangladeshi cities using Google ADK.

## Quick Start

```bash
# From repository root with venv activated
python3 1_single_agent/main.py
```

## Project Structure

```
1_single_agent/
├── config/
│   └── settings.py      # Model, cities, retry configuration
├── tools/
│   └── time_tools.py    # Tool functions (get_current_time)
├── agents/
│   └── root_agent.py    # Agent definition
├── services/
│   └── runner.py        # Runner + response extraction
└── main.py              # Entry point
```

## Configuration

All settings are centralized in `config/settings.py`:

| Setting | Default | Description |
|---------|---------|-------------|
| `MODEL_NAME` | `gemini-2.5-flash` | Model to use |
| `CITY_TIMEZONES` | Dhaka, Chittagong, Chattogram | Supported cities |
| `RETRY_OPTIONS` | 5 attempts, exponential backoff | HTTP retry config |

## Supported Cities

- Dhaka
- Chittagong (Chattogram)

Timezone: `Asia/Dhaka`

## Agent Details

- **Model**: gemini-2.5-flash
- **Tools**: `get_current_time` - returns current time in specified city
- **Features**: Automatic retry on 429/500/503/504 errors