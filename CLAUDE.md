# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python project called `hello-langextract` that uses the `langextract` library. The project is managed with UV, a modern Python package manager.

## Development Commands

### Environment Setup
```bash
# Install dependencies
uv sync

# Run the main application
uv run main.py
```

### Dependency Management
```bash
# Add a new dependency
uv add <package-name>

# Add a development dependency
uv add --dev <package-name>

# Update dependencies
uv sync
```

## Project Structure

The project is a single-module Python application with the following key files:
- `main.py` - Entry point of the application
- `pyproject.toml` - Project configuration and dependencies (`[tool.uv] exclude-newer = "7 days"` only resolves packages published at least 7 days ago)
- `uv.lock` - Locked dependency versions
- `.python-version` - Pins Python 3.14.8 (`requires-python = ">=3.14"`)
- `aqua.yaml` - Pins CLI tools including uv (CI installs uv via aqua, then Python via `uv python install`)

## Key Dependencies

- **langextract** (==1.0.3, pinned) - The main library providing language extraction capabilities
  - Includes AI/ML integrations (Google GenAI, OpenAI)
  - HTTP client libraries (aiohttp, httpx, requests)
  - Data processing tools (numpy, pandas, pydantic)

## Architecture Notes

Currently, this is a minimal setup with just a basic "Hello World" implementation. The project is designed to utilize the `langextract` library for language extraction and processing tasks, but the main functionality is not yet implemented.

When implementing features:
- The `langextract` library provides AI/ML capabilities through various provider integrations
- Consider using async patterns as the dependencies include async HTTP libraries
- Environment configuration can be managed via python-dotenv (included in dependencies)