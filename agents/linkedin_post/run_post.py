#!/usr/bin/env python3
"""
Runner for the LinkedIn Post Helper Agent
"""

from dotenv import load_dotenv
load_dotenv()  # loads GOOGLE_API_KEY and others from .env

from agents.linkedin_post.agent import root_agent

if __name__ == "__main__":
    print("💼 LinkedIn Post Helper Agent ✍️")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You (idea for post): ")
        if user_input.lower().strip() in {"exit", "quit"}:
            print("Goodbye 👋")
            break

        # Call the agent
        response = root_agent.respond(user_input)

        # Handle different ADK return types
        if hasattr(response, "text"):
            print("\n📢 Draft Post:\n")
            print(response.text)
        else:
            print("\n📢 Draft Post:\n")
            print(response)
        print("-" * 60)
