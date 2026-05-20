# Ollama Tool Calling

A Python project demonstrating tool calling with Ollama, 
Tools implemented
- Secure SMTP email tool.

## Features

- Tool calling with Ollama models
- Secure email sending via SMTP with TLS
- Environment-based configuration (credentials not in code)
- Jupyter notebook examples

## Setup

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Configure environment:
   ```bash
   cp .env.example .env
   # Edit .env with your SMTP settings
   ```

3. Run the notebook:
   ```bash
   jupyter notebook tool_calling_with_ollama1.ipynb
   ```

## Project Structure

- `my_tools.py` - Tool definitions and implementations
- `tool_calling_with_ollama1.ipynb` - Example usage
- `.env` - Configuration (not committed)
- `.env.example` - Configuration template

## Requirements

- Python 3.12+
- Ollama with a compatible model (e.g., granite4.1:8b)