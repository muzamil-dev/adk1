#!/usr/bin/env python3
"""
Runner script for the Resume Optimizer Agent System
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
from agents.resume_optimizer.agent import root_agent

async def run_resume_optimizer():
    """
    Example run of the resume optimization pipeline
    """
    
    # Initialize services
    session_service = InMemorySessionService()
    
    # Create runner
    runner = Runner(
        agent=root_agent,
        app_name="resume_optimizer_app",
        session_service=session_service
    )
    
    # Create session
    session_id = "resume_optimizer_session"
    user_id = "user1"
    
    await runner.session_service.create_session(
        app_name="resume_optimizer_app", 
        user_id=user_id, 
        session_id=session_id
    )
    
    # Example input with current resume and target role
    user_input = Content(
        parts=[Part(text="""
        Please optimize my resume for better impact and ATS compatibility.
        
        Current Resume:
        
        **John Smith**
        Email: john.smith@email.com | Phone: (555) 123-4567
        
        **Summary**
        Software developer with experience in web development.
        
        **Experience**
        Software Developer - Tech Company (2021-2024)
        - Worked on web applications
        - Used JavaScript and Python
        - Collaborated with team members
        - Fixed bugs and added features
        
        Junior Developer - StartupCorp (2019-2021)  
        - Developed websites
        - Learned new technologies
        - Helped with projects
        
        **Education**
        Bachelor of Science in Computer Science
        State University, 2019
        
        **Skills**
        JavaScript, Python, HTML, CSS, Git
        
        Target Role: Senior Full-Stack Developer positions at mid-size tech companies
        
        Please analyze and optimize this resume for maximum impact.
        """)], 
        role="user"
    )
    
    print("🚀 Starting Resume Optimization Pipeline...")
    print("=" * 60)
    print("   Stage 1: Analyzing current resume...")
    print("   Stage 2: Generating optimization recommendations...")
    print("   Stage 3: Creating final optimized resume...")
    print()
    
    # Run the pipeline
    final_response = ""
    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=user_input):
        if event.is_final_response() and event.content and event.content.parts:
            final_response = event.content.parts[0].text
            print("✅ Pipeline Complete!")
            print("=" * 60)
            print("📄 Optimized Resume:")
            print("=" * 60)
            print(final_response)
            print("=" * 60)

if __name__ == "__main__":
    print("Resume Optimizer Agent System")
    print("=" * 60)
    asyncio.run(run_resume_optimizer())