#!/usr/bin/env python3
"""
Test scenarios for the Cover Letter Drafter Agent System
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

class CoverLetterTestRunner:
    def __init__(self):
        self.session_service = InMemorySessionService()
        
    async def run_scenario(self, scenario_name, resume_background, job_opportunity):
        """Run a single cover letter generation scenario"""
        
        print(f"\n🎯 Scenario: {scenario_name}")
        print("=" * 80)
        
        # Create runner
        runner = Runner(
            agent=root_agent,
            app_name="cover_letter_app",
            session_service=self.session_service
        )
        
        # Create unique session for this scenario
        session_id = f"session_{scenario_name.lower().replace(' ', '_')}"
        user_id = "test_user"
        
        await runner.session_service.create_session(
            app_name="cover_letter_app",
            user_id=user_id,
            session_id=session_id
        )
        
        # Prepare input
        user_input = Content(
            parts=[Part(text=f"""
            Please create a cover letter for me.
            
            My Resume Background:
            {resume_background}
            
            Job Opportunity:
            {job_opportunity}
            
            Please draft a professional cover letter for this position.
            """)],
            role="user"
        )
        
        print("🔄 Processing through pipeline...")
        print("   Stage 1: Drafting cover letter...")
        print("   Stage 2: Reviewing for best practices...")
        print("   Stage 3: Creating final polished version...")
        print()
        
        # Run the pipeline
        final_response = ""
        async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=user_input):
            if event.is_final_response() and event.content and event.content.parts:
                final_response = event.content.parts[0].text
                
        print("✅ Final Cover Letter:")
        print("-" * 80)
        print(final_response)
        print("-" * 80)
        return final_response

async def main():
    """Run multiple test scenarios"""
    
    print("🚀 Cover Letter Drafter Agent System - Test Scenarios")
    print("=" * 80)
    
    runner = CoverLetterTestRunner()
    
    # Scenario 1: Software Engineer
    await runner.run_scenario(
        "Software Engineer Position",
        """
        - 3 years of full-stack development experience
        - Proficient in Python, JavaScript, and SQL
        - Built and deployed 5+ web applications
        - Experience with AWS cloud services
        - Strong debugging and optimization skills
        - Computer Science degree from State University
        """,
        """
        Software Engineer at InnovateTech Solutions
        - Develop scalable web applications
        - Work with microservices architecture
        - Collaborate in agile environment
        - Company values: Innovation, collaboration, continuous learning
        - Growing startup in the fintech space
        """
    )
    
    # Scenario 2: Marketing Manager
    await runner.run_scenario(
        "Marketing Manager Position", 
        """
        - 6 years of digital marketing experience
        - Led campaigns with $500K+ budgets
        - Expertise in SEO, SEM, and social media marketing
        - Increased brand awareness by 150% at previous company
        - MBA in Marketing from Business School
        - Strong analytical and leadership skills
        """,
        """
        Senior Marketing Manager at GrowthCorp
        - Lead digital marketing initiatives
        - Manage marketing team of 8 people
        - Develop go-to-market strategies for new products
        - Company mission: Helping small businesses grow online
        - Fast-paced environment with opportunity for advancement
        """
    )
    
    # Scenario 3: Data Analyst
    await runner.run_scenario(
        "Data Analyst Position",
        """
        - 4 years of data analysis experience
        - Expert in Python, R, and SQL
        - Created dashboards and reports for C-level executives
        - Experience with machine learning and statistical modeling
        - Published research in data science conferences
        - Master's degree in Statistics
        """,
        """
        Senior Data Analyst at DataDriven Inc.
        - Analyze large datasets to drive business decisions
        - Build predictive models and forecasting systems
        - Present insights to stakeholder teams
        - Remote-first company with strong data culture
        - Opportunity to work on cutting-edge AI projects
        """
    )
    
    print("\n🎉 All test scenarios completed!")
    print("The cover letter pipeline successfully handled different job types and backgrounds.")

if __name__ == "__main__":
    asyncio.run(main())