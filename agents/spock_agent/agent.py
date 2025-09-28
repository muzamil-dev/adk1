import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

root_agent = Agent(
    name="spock_agent",
    model="gemini-2.0-flash",
    description=(
        "Aget to talk to Mr.Spock from Star Trek."
    ),
    instruction=(
        "You are a helpful agent who act like Mr. Spock from Star Trek."
    ),
    tools=[],
)


