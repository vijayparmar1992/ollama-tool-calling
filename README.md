# Ollama Tool Calling

A Python project demonstrating tool calling with Ollama.

The current example lets a local Ollama model decide when to call a Python tool for sending email through SMTP.

## Features

- Tool calling with Ollama models
- Secure email sending via SMTP with TLS
- Environment-based configuration (credentials not in code)
- Reusable notebook helper function: `chat_with_tools()`
- Jupyter notebook example

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

4. Run the example prompt in the notebook:
   ```python
   user_message = "please send mail to example@example.com with subject 'Hello' and message 'Hello, how are you?'"
   chat_with_tools(user_message)
   ```

## How It Works

1. The user message is sent to `ollama.chat()` with the tool schema from `my_tools.py`.
2. If the model returns a tool call, the notebook looks up the matching Python function in `AVAILABLE_FUNCTIONS`.
3. The function runs locally and returns a JSON result.
4. The tool result is sent back to the model for a final assistant response.

## Project Structure

- `my_tools.py` - Tool definitions and implementations
- `tool_calling_with_ollama1.ipynb` - Reusable tool-calling example with `chat_with_tools()`
- `.env` - Configuration (not committed)
- `.env.example` - Configuration template

## Requirements

- Python 3.12+
- Ollama with a compatible model (e.g., granite4.1:8b)
