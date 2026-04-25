# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains AI agents built with Google's ADK (Agent Development Kit). The main example is a single agent that tells the current time in Bangladeshi cities (Dhaka, Chittagong/Chattogram).

## Development Commands

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS

# Install dependencies
pip install -r requirements.txt

# Run the single agent example
python3 1_single_agent/main.py
```

## Project Structure

```
1_single_agent/           # Main agent implementation
├── main.py              # Entry point using InMemoryRunner
└── agent/
    └── agent.py         # Agent definition with get_current_time tool

scripts/                  # Utility scripts
claude-certifications/    # Learning notes
```

## Key Details

- Uses Google ADK's `InMemoryRunner` for agent execution
- The root agent uses `gemini-2.5-flash` model with a custom `get_current_time` tool
- Configuration via environment variables loaded from `.env` (see `.env.example`)
- Retry configuration handles rate limits (429) and server errors (500, 503, 504)