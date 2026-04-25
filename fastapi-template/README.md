# FastAPI Template

A minimal FastAPI project template built with uv.

## Quick Start

```bash
# Install dependencies
uv sync

# Run development server
uv run uvicorn main:app --reload
```

The API will be available at http://localhost:8000

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check

## Project Structure

```
fastapi-template/
├── main.py          # Application entry point
├── pyproject.toml   # Project configuration
└── .venv/           # Virtual environment
```

## Commands

```bash
# Run with different host/port
uv run uvicorn main:app --host 0.0.0.0 --port 8080

# Run with auto-reload
uv run uvicorn main:app --reload

# Add dependencies
uv add <package>
```