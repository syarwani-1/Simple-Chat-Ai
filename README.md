# Groq Chat Terminal

## Overview
A simple terminal-based chat using Groq AI for conversational interactions.

## Prerequisites
- Python 3.8+
- Groq API Key

## Installation

### Dependencies
```bash
pip install python-dotenv groq
```

### Termux Installation
If using Termux, first install Rust:
```bash
pkg install rust
pkg install python
pip install python-dotenv groq
```

## API Key Setup
1. Create an account at [Groq Console](https://console.groq.com/)
2. Generate your API key
3. Create a `.env` file in the project directory
4. Add your API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Configuration
- Modify `temperature` to adjust response creativity
- Change `max_tokens` to control response length
- Select different Groq AI models as needed
- Customize the system instructions as you like [Change here](https://github.com/syarwani-1/Simple-Chat-Ai/blob/adbad9f986cc38da816c860ef628a018269d2aec/chat_ai.py#L15)

## Running the Application
```bash
python chat_ai.py
```

### Usage
- Type your messages normally
- Type `exit`, `quit`, or `bye` to end the conversation

## Troubleshooting
- Verify Python installation
- Check API key validity
- Ensure internet connectivity
