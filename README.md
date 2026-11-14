# Week 2 Day 5 – LangChain: Breakfast Ideas

## Project Overview
A simple LangChain application that uses an OpenAI chat model to generate exactly five healthy breakfast ideas.

## Technologies Used
- Python
- LangChain
- LangChain OpenAI
- python-dotenv
- OpenAI GPT-4o-mini

## Implementation
The application:
1. Loads the OpenAI API key from an environment variable using a shared `.env` file.
2. Initializes the LangChain `ChatOpenAI` model.
3. Sends a prompt requesting exactly five healthy breakfast ideas.
4. Uses `llm.invoke()` to generate the response.
5. Prints only the response text using `reply.content`.

## Run the Application

```bash
python breakfast.py
```

## Experiment and Observation

The application was executed twice using the same prompt and model.

**Observation:** Both executions generated five healthy breakfast ideas, but the suggestions were different.

This demonstrates that LLM responses can vary even when the same prompt and model are used.

## Project File

`breakfast.py` – Contains the complete LangChain implementation.

## Learning Outcome

Understood how to initialize a LangChain chat model, send prompts using `invoke()`, access the response through `.content`, and observe variation in LLM-generated outputs.