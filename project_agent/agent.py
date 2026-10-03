from google.adk.agents.llm_agent import Agent

def get_current_time(city: str) -> dict:
    """Return the current time in a specified city"""
    return {"status": "success", "city": city, "time": "10:30 AMs"}

root_agent = Agent(
    model='gemini-3.8-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[get_current_time],
)
