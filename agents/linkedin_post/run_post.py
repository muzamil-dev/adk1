#!/usr/bin/env python3
"""
Runner for the LinkedIn Post Helper Agent
"""

from .agent import root_agent

if __name__ == "__main__":
    print("💼 LinkedIn Post Helper Agent ✍️")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You (idea for post): ")
        if user_input.lower().strip() in {"exit", "quit"}:
            print("Goodbye 👋")
            break

        # Generate post draft from your agent
        response = root_agent.generate(user_input)

        # Depending on ADK version, response may be Content/Part or plain text
        if hasattr(response, "text"):
            print("\n📢 Draft Post:\n")
            print(response.text)
        else:
            print("\n📢 Draft Post:\n")
            print(response)
        print("-" * 60)
