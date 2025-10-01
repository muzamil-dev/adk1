from .agent import root_agent

if __name__ == "__main__":
    print("🌦️ Weather & Time Agent 🕒")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in {"exit", "quit"}:
            print("Goodbye 👋")
            break

        # Use the executor API
        result = root_agent.execute(input=user_input)
        print("Agent:", result.output)
