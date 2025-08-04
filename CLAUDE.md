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
- `pyproject.toml` - Project configuration and dependencies
- `uv.lock` - Locked dependency versions
- `.python-version` - Specifies Python 3.11

## Key Dependencies

- **langextract** (>=1.0.3) - The main library providing language extraction capabilities
  - Includes AI/ML integrations (Google GenAI, OpenAI)
  - HTTP client libraries (aiohttp, httpx, requests)
  - Data processing tools (numpy, pandas, pydantic)

## Architecture Notes

Currently, this is a minimal setup with just a basic "Hello World" implementation. The project is designed to utilize the `langextract` library for language extraction and processing tasks, but the main functionality is not yet implemented.

When implementing features:
- The `langextract` library provides AI/ML capabilities through various provider integrations
- Consider using async patterns as the dependencies include async HTTP libraries
- Environment configuration can be managed via python-dotenv (included in dependencies)