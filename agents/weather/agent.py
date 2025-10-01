import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
import requests

# Base URL for Glax Weather API
GLAX_WEATHER_BASE = "https://dragon.best/api/glax_weather.json"


def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    # Build request parameters for the Glax Weather API
    params = {
        "location": city,
        "units": "metric",   # metric = Celsius, you could switch to "imperial"
        "forecast": "off",   # "on" returns forecast as well
    }

    try:
        # Make the API call
        resp = requests.get(GLAX_WEATHER_BASE, params=params, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        # Return a friendly error if the network call fails
        return {"status": "error", "error_message": f"API error: {e}"}

    data = resp.json()

    # Try to parse expected keys — this may need tweaking depending on API response
    current = data.get("current") or {}
    desc = current.get("condition") or current.get("description", "unknown")
    temp = current.get("temp_c") or current.get("temp")

    # If no temp is found, return raw data for debugging
    if temp is None:
        return {
            "status": "error",
            "error_message": "Temperature not found in API response.",
            "raw": data,
        }

    # Build the human-readable report
    report = f"The weather in {city} is {desc} with temperature {temp}°C."
    return {"status": "success", "report": report, "raw": data}


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": f"Sorry, I don't have timezone information for {city}.",
        }

    # Get timezone object
    tz = ZoneInfo(tz_identifier)

    # Get current time in that timezone
    now = datetime.datetime.now(tz)
    report = f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    return {"status": "success", "report": report}


# Register the agent with ADK
root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description="Agent to answer questions about the time and weather in a city.",
    instruction="You are a helpful agent who can answer user questions about the time and weather in a city.",
    tools=[get_weather, get_current_time],
)
