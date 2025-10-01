#!/usr/bin/env python3
"""
Runner script for the Weather & Time Agent System
"""

import asyncio
import sys
import os

# Add the parent directory to path so we can import agents
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from agents.weather.agent import root_agent


async def run_weather_agent():
    """
    Run the weather & time agent interactively.
    """

    # Initialize services
    session_service = InMemorySessionService()

    # Create runner
    runner = Runner(
        agent=root_agent,
        app_name="weather_time_app",
        session_service=session_service
    )

    # Create session
    session_id = "weather_time_session"
    user_id = "user1"

    await runner.session_service.create_session(
        app_name="weather_time_app",
        user_id=user_id,
        session_id=session_id
    )

    print("🌦️ Weather & Time Agent 🕒")
    print("Type 'exit' to quit.")
    print("=" * 60)

    while True:
        user_input_text = input("You: ")
        if user_input_text.lower().strip() in {"exit", "quit"}:
            print("Goodbye 👋")
            break

        user_input = Content(parts=[Part(text=user_input_text)], role="user")

        async for event in runner.run_async(
            user_id=user_id,
            session_id=session_id,
            new_message=user_input
        ):
            if event.is_final_response() and event.content and event.content.parts:
                print("Agent:", event.content.parts[0].text)


if __name__ == "__main__":
    asyncio.run(run_weather_agent())
