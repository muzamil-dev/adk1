
from google.adk.agents import Agent
from google.adk.agents import Agent, LlmAgent,SequentialAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types
from zoneinfo import ZoneInfo
import datetime

root_agent = Agent(
    name="blogger_outline_agent",
    model="gemini-2.0-flash",
    description="Agent to outline a blog post series on a specific theme.",
    instruction="I can help you outline a series of blog posts on a specific theme. Just provide me with the theme and I'll create an outline for you!",
    tools=[google_search],
    output_key="blog_series_outline"
)



 

