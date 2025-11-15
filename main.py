import os
from dotenv import load_dotenv

load_dotenv()

langsmith_tracing = os.getenv("LANGSMITH_TRACING")
langsmith_endpoint= os.getenv("LANGSMITH_ENDPOINT")
langsmith_api_key = os.getenv("LANGSMITH_API_KEY")
langsmith_project= os.getenv("LANGSMITH_PROJECT")
openai_api_key = os.getenv("OPENAI_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

print(langsmith_tracing)
print(langsmith_endpoint)
print(langsmith_api_key)
print(langsmith_project)
print(openai_api_key)
print(anthropic_api_key)

from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic

claude_haiku = ChatAnthropic(
	model="claude-haiku-4-5-20251001",
	temperature=0.5,
	max_tokens=8192,
	timeout=None,
	max_retries=2,
)

def get_weather(city: str) -> str:
	"""Get weather for a given city."""
	return f"It's always sunny in {city}"

def get_air_quality(city: str) -> str:
	"""Get air quality for a given city."""
	return f"It's always windy in {city}"

agent = create_agent(
	model=claude_haiku,
	tools=[get_weather, get_air_quality],
	system_prompt="You are a helpful assistant.",
)

agent.invoke(
	{"messages": [{"role": "user", "content": "How is the general weather and air quality in San Francisco?"}]}
)