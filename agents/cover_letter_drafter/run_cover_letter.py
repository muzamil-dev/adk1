#!/usr/bin/env python3
"""
Runner script for the Cover Letter Drafter Agent System
"""

import asyncio
import sys
import os

# Add the parent directory to path to import agents
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from agents.cover_letter_drafter.agent import root_agent

async def run_cover_letter_pipeline():
    """
    Example run of the cover letter drafting pipeline
    """
    
    # Initialize services
    session_service = InMemorySessionService()
    
    # Create runner
    runner = Runner(
        agent=root_agent,
        app_name="cover_letter_app",
        session_service=session_service
    )
    
    # Create session
    session_id = "cover_letter_session"
    user_id = "user1"
    
    await runner.session_service.create_session(
        app_name="cover_letter_app", 
        user_id=user_id, 
        session_id=session_id
    )
    
    # Example input with resume background and job opportunity
    user_input = Content(
        parts=[Part(text="""
        Please create a cover letter for me.
        
        My Resume Background:
        - 5+ years of software engineering experience
        - Expertise in Python, React, and Node.js
        - Led development of 3 major web applications
        - Experience with agile methodologies and team leadership
        - Bachelor's degree in Computer Science
        - Strong problem-solving and communication skills
        
        Job Opportunity:
        Senior Frontend Developer at TechCorp
        - Build responsive web applications using React
        - Collaborate with design and backend teams
        - Mentor junior developers
        - Work with modern JavaScript frameworks
        - Remote-friendly company focused on innovation
        - Company mission: Making technology accessible to everyone
        
        Please draft a professional cover letter for this position.
        """)], 
        role="user"
    )
    
    print("🚀 Starting Cover Letter Pipeline...")
    print("=" * 60)
    
    # Run the pipeline
    final_response = ""
    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=user_input):
        if event.is_final_response() and event.content and event.content.parts:
            final_response = event.content.parts[0].text
            print("✅ Pipeline Complete!")
            print("=" * 60)
            print("📄 Final Cover Letter:")
            print("=" * 60)
            print(final_response)
            print("=" * 60)

if __name__ == "__main__":
    print("Cover Letter Drafter Agent System")
    print("=" * 60)
    asyncio.run(run_cover_letter_pipeline())