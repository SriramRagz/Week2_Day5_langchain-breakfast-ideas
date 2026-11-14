# Week 2 Day 5 – Ask LangChain for 5 Breakfast Ideas

## Project Overview
A simple Python application built using LangChain and OpenAI that generates five healthy breakfast ideas.

## Technologies Used
- Python
- LangChain
- OpenAI GPT-4o-mini
- python-dotenv

## How It Works
1. Loads the OpenAI API key from an environment file.
2. Initializes the ChatOpenAI model.
3. Sends a prompt requesting exactly five healthy breakfast ideas.
4. Displays the model response in the terminal.

## How to Run
```bash
python breakfast.py
```

## Testing and Observation
The application was executed twice using the same prompt. Both runs generated five healthy breakfast suggestions, but the suggestions varied between runs.

## Project Files
- `breakfast.py` – Main application
- `requirements.txt` – Python dependencies
- `.gitignore` – Excludes private and unnecessary files
- `screenshots/` – Execution screenshots

## Learning Outcomes
- Understanding LangChain's ChatOpenAI integration.
- Using prompts to guide model responses.
- Loading API keys securely using environment variables.
- Invoking an LLM using `llm.invoke()`.
- Observing variations in model-generated responses.