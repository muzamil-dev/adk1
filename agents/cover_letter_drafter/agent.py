from google.adk.agents import Agent, LlmAgent, SequentialAgent
from google.adk.tools import google_search

cover_letter_drafter_agent = Agent(
    name="cover_letter_drafter_agent",
    model="gemini-2.0-flash",
    description="Agent to draft a compelling cover letter based on resume background and job opportunity.",
    instruction="""
I can draft a professional and compelling cover letter tailored to a specific job opportunity. 
Provide me with:
1. Your resume background/experience
2. The job opportunity details (link or description)

I will create a personalized cover letter that:
- Highlights relevant experience and skills
- Shows enthusiasm for the role and company
- Demonstrates knowledge of the company and position
- Uses professional tone and proper formatting
- Follows standard cover letter structure (opening, body, closing)
- Is concise but impactful (typically 3-4 paragraphs)

**Key elements I include:**
- Strong opening that mentions the specific position
- Connection between your background and job requirements
- Specific examples of relevant achievements
- Company research and why you want to work there
- Professional closing with call to action
    """,
    tools=[google_search],
    output_key="cover_letter_draft"
)

cover_letter_reviewer_agent = Agent(
    name="cover_letter_reviewer_agent", 
    model="gemini-2.0-flash",
    description="Agent to review cover letters and ensure they follow best practices.",
    instruction="""
I review cover letters to ensure they follow best practices for job applications.
I will analyze the cover letter and provide specific feedback on:

**Structure & Format:**
- Professional header with contact information
- Proper business letter format
- Appropriate length (1 page, 3-4 paragraphs)
- Clear paragraph structure

**Content Quality:**
- Strong, engaging opening
- Specific examples and achievements
- Relevance to the job requirements
- Company knowledge demonstration
- Professional closing

**Writing Style:**
- Clear, concise language
- Active voice usage
- Professional tone
- Error-free grammar and spelling
- Appropriate formality level

**Cover Letter to Review:**
{cover_letter_draft}

I will provide specific, actionable feedback as bullet points for improvement.
    """,
    tools=[google_search],
    output_key="review_feedback"
)

cover_letter_editor_agent = Agent(
    name="cover_letter_editor_agent",
    model="gemini-2.0-flash", 
    description="Agent to create the final polished cover letter based on review feedback.",
    instruction="""
I create the final, polished version of a cover letter by incorporating review feedback.
I will take the original draft and the reviewer's comments to produce a refined, professional cover letter.

**Original Cover Letter Draft:**
{cover_letter_draft}

**Review Feedback to Incorporate:**
{review_feedback}

I will:
- Address all the feedback points
- Maintain the professional tone and structure
- Ensure proper formatting and flow
- Create a compelling final version ready for submission
- Keep the letter concise and impactful
- Return the final cover letter in professional format

The final output will be a polished, job-ready cover letter.
    """,
    tools=[google_search],
    output_key="final_cover_letter"
)

cover_letter_pipeline_agent = SequentialAgent(
    name="CoverLetterPipelineAgent",
    sub_agents=[
        cover_letter_drafter_agent,
        cover_letter_reviewer_agent, 
        cover_letter_editor_agent
    ],
    description="Complete cover letter creation pipeline: drafts, reviews, and finalizes cover letters."
)

root_agent = cover_letter_pipeline_agent


