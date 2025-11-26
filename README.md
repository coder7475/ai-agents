# AI Agents

This repository contains various AI agents developed for different purposes.

## Usage

### 1 Create and activate venv

```bash
# create venv
python3 -m venv .venv

# activate (Linux/macOS)
source .venv/bin/activate

# on Windows PowerShell
# .venv\Scripts\Activate.ps1
```

This makes `.venv` local to the repo and isolates packages from the system.[3][2]

### 2 Install required packages

With pip:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Using `uv` as a faster drop-in (optional):

```bash
uv pip install -r requirements.txt
```

The `requirements.txt` you already defined (`pydantic`, `pydantic-settings`, `python-dotenv`) will now be installed inside `.venv`, and any script run from the activated venv can import `config` and use `get_settings()`.