# AI Agents

This repository contains various AI agents developed using Google's ADK (Agent Development Kit).

## Project Structure

```
.
├── 1_single_agent/       # Single agent implementation
│   ├── config/           # Configuration settings
│   ├── tools/            # Agent tools
│   ├── agents/           # Agent definitions
│   ├── services/         # Runner and execution logic
│   └── main.py           # Entry point
├── fastapi-template/     # FastAPI project template
├── scripts/              # Utility scripts
└── requirements.txt      # Shared dependencies
```

## Setup

### 1. Create and activate venv

```bash
# create venv
python3 -m venv .venv

# activate (Linux/macOS)
source .venv/bin/activate

# on Windows PowerShell
# .venv\Scripts\Activate.ps1
```

### 2. Install required packages

```bash
# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Or using `uv` (faster drop-in replacement):

```bash
uv pip install -r requirements.txt
```

## Running Agents

### Single Agent

A simple agent that tells the current time in Bangladeshi cities.

```bash
python3 1_single_agent/main.py
```

Configuration can be modified in `1_single_agent/config/settings.py`.

## References

1. [5 days of Intensive AI Agents Intensive](https://www.kaggle.com/learn-guide/5-day-agents)
2. [Agentic AI](https://agenticai-learning.org/f25)
3. [ADK Documentation](https://google.github.io/adk-docs/get-started/)