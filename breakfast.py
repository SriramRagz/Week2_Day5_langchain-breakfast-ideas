
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load API key from environment
load_dotenv("../.env", override=True)

# Initialize LangChain model
llm = ChatOpenAI(model="gpt-4o-mini")

# Define the prompt
prompt = """
Suggest exactly 5 healthy breakfast ideas.

Consider these criteria for healthy:
- Include nutritious ingredients.
- Prefer whole grains, fruits, vegetables and protein.
- Avoid excessive added sugar and unhealthy fats.

Output requirements:
- Number the ideas from 1 to 5.
- Keep each idea to one line.
- Do not include an introduction or conclusion.
- Return exactly 5 ideas.
"""

# Invoke the model
reply = llm.invoke(prompt)

# Print only the response text
print(reply.content)
