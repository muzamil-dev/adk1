"""
LinkedIn Post Helper Agent

This agent helps create engaging LinkedIn posts from user-provided ideas.
It generates posts with a hook, main body, call-to-action, and suggested hashtags.
"""

from google.adk.agents import Agent

# Define the LinkedIn Post Helper Agent
root_agent = Agent(
    name="linkedin_post_helper",
    model="gemini-2.0-flash",
    description="Agent that drafts engaging LinkedIn posts from rough ideas or bullet points.",
    instruction=(
        "You are a helpful LinkedIn Post Assistant. "
        "When given a topic or idea, generate a polished LinkedIn post. "
        "Always include:\n"
        "1. A strong hook (first line, attention-grabber)\n"
        "2. Main body (2–3 short paragraphs)\n"
        "3. A closing call-to-action (ask a question or invite engagement)\n"
        "4. Suggested hashtags (3–6 relevant ones)\n\n"
        "Keep the tone professional yet conversational. "
        "Adapt the style to the user’s request (e.g., storytelling, casual, thought-leader)."
    ),
)
