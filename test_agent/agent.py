from google.adk.agents.llm_agent import Agent
import weatherkit

def get_current_weather(latitude: float, longitude: float) -> dict:
    """Finds the current weather for the given latitude and logitude location,
    if the user provides a city name fetch the appropriate latitude and logitude for the calculation.
    """
    weather = weatherkit.current_weather(latitude, longitude)
    return {"message": "success", 
           "weather": weather.temperature(), 
           "humidity": weather.humidity(),
           "precipitation": weather.precipitation()
    }

root_agent = Agent(
    name = "Test_Agent",
    model = "gemini-flash-latest",
    description = "You are a helpful assistant that answers back in terse language",
    instruction = """Given latitude and longitude find out 
    the city and print it in your output or if city name is mentioned 
    pass latitude and longitiude in the 
    appropriate tool to find out the weather""",
    tools=[get_current_weather],
)