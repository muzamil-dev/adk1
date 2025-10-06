#!/usr/bin/env python3
"""
Runner script for the Email Assistant Agent System
"""

import asyncio
import sys
import os

# Add the project root to path to import agents
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not available, environment variables should be set manually

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from agents.email_assistant.agent import root_agent

async def run_email_assistant():
    """
    Example run of the email assistant pipeline
    """
    
    # Initialize services
    session_service = InMemorySessionService()
    
    # Create runner
    runner = Runner(
        agent=root_agent,
        app_name="email_assistant_app",
        session_service=session_service
    )
    
    # Create session
    session_id = "email_assistant_session"
    user_id = "user1"
    
    await runner.session_service.create_session(
        app_name="email_assistant_app", 
        user_id=user_id, 
        session_id=session_id
    )
    
    # Example input for a professional follow-up email
    user_input = Content(
        parts=[Part(text="""
        Please help me draft a professional email.
        
        Email Context:
        - Purpose: Follow up on job interview from last week
        - Recipient: Sarah Johnson, Hiring Manager at TechCorp
        - Relationship: Professional, had a great 1-hour interview
        - Tone: Professional but warm, expressing continued interest
        
        Key Points to Include:
        - Thank her for the interview time
        - Reiterate my interest in the Senior Developer position
        - Mention the specific project we discussed (mobile app redesign)
        - Offer to provide additional information if needed
        - Ask about next steps and timeline
        
        Additional Context:
        - Interview was on Monday, today is Friday
        - She mentioned they're looking to fill the position quickly
        - We had good rapport discussing React and mobile development
        - Company culture seemed very collaborative
        
        Please create a professional follow-up email that will help keep me top-of-mind for this position.
        """)], 
        role="user"
    )
    
    print("📧 Starting Email Assistant Pipeline...")
    print("=" * 60)
    print("   Stage 1: Drafting professional email...")
    print("   Stage 2: Reviewing for effectiveness and tone...")
    print("   Stage 3: Creating final polished version...")
    print()
    
    # Run the pipeline
    final_response = ""
    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=user_input):
        if event.is_final_response() and event.content and event.content.parts:
            final_response = event.content.parts[0].text
            print("✅ Pipeline Complete!")
            print("=" * 60)
            print("📨 Final Email:")
            print("=" * 60)
            print(final_response)
            print("=" * 60)

if __name__ == "__main__":
    print("Email Assistant Agent System")
    print("=" * 60)
    asyncio.run(run_email_assistant())