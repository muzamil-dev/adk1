"""
Integration example: Using the Cover Letter Drafter in the main agent runner
"""

import asyncio
import sys
import os

# Add agents to path
sys.path.append('/workspaces/adk1')

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from agents.cover_letter_drafter.agent import root_agent as cover_letter_agent

async def main():
    """
    Example of integrating the cover letter drafter into a larger system
    """
    
    # Initialize services (these could be shared across multiple agents)
    session_service = InMemorySessionService()
    
    # Create runner with the cover letter agent
    runner = Runner(
        agent=cover_letter_agent,
        app_name="job_application_assistant",
        session_service=session_service
    )
    
    # Create session
    await runner.session_service.create_session(
        app_name="job_application_assistant",
        user_id="job_seeker_123",
        session_id="cover_letter_session"
    )
    
    # Example user input
    user_message = Content(
        parts=[Part(text="""
        I need a cover letter for a Product Manager position.
        
        My background:
        - 7 years of product management experience
        - Led cross-functional teams of up to 15 people
        - Launched 10+ successful products with $50M+ revenue
        - Expert in agile methodologies and user research
        - MBA from Top Business School
        - Strong analytical and strategic thinking skills
        
        Job details:
        Senior Product Manager at CloudTech Innovations
        - Lead product strategy for cloud infrastructure products
        - Manage product roadmap and prioritization
        - Work closely with engineering and design teams
        - Company focus: Enterprise cloud solutions
        - Fast-growing company valued at $2B
        - Remote-first culture with emphasis on innovation
        
        Please create a compelling cover letter for this role.
        """)],
        role="user"
    )
    
    print("🚀 Generating cover letter...")
    
    # Process through the pipeline
    async for event in runner.run_async(
        user_id="job_seeker_123", 
        session_id="cover_letter_session", 
        new_message=user_message
    ):
        if event.is_final_response() and event.content and event.content.parts:
            print("✅ Cover letter generated successfully!")
            print("\n" + "="*80)
            print("FINAL COVER LETTER:")
            print("="*80)
            print(event.content.parts[0].text)
            print("="*80)

if __name__ == "__main__":
    asyncio.run(main())