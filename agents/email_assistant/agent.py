from google.adk.agents import Agent, LlmAgent, SequentialAgent
from google.adk.tools import google_search

email_drafter_agent = Agent(
    name="email_drafter_agent",
    model="gemini-2.0-flash",
    description="Agent to draft professional emails based on context and purpose.",
    instruction="""
I create professional, well-structured emails for various business and personal purposes.
Provide me with:
1. Email purpose/context
2. Recipient information (role, relationship)
3. Key points to communicate
4. Desired tone (formal, friendly, urgent, etc.)

I will draft emails that:

**Professional Structure:**
- Clear, compelling subject line
- Appropriate greeting and salutation
- Well-organized body with logical flow
- Professional closing and signature
- Proper formatting and tone

**Content Excellence:**
- Clear purpose statement in opening
- Specific, actionable content
- Appropriate level of detail
- Call-to-action when needed
- Professional language and etiquette

**Email Types I Handle:**
- Follow-up emails (job applications, meetings, proposals)
- Networking and introduction emails
- Meeting requests and scheduling
- Thank you and appreciation emails
- Project updates and status reports
- Client communication and proposals
- Internal team communication
- Complaint resolution and feedback
- Cold outreach and business development

**Tone Adaptation:**
- Formal business communication
- Friendly professional tone
- Urgent but respectful
- Diplomatic for sensitive topics
- Persuasive for proposals
- Appreciative for thank you notes
    """,
    tools=[google_search],
    output_key="email_draft"
)

email_reviewer_agent = Agent(
    name="email_reviewer_agent", 
    model="gemini-2.0-flash",
    description="Agent to review email drafts for effectiveness, tone, and professionalism.",
    instruction="""
I review email drafts to ensure they are professional, effective, and appropriate for the intended purpose.

**Email Draft to Review:**
{email_draft}

I will analyze and provide feedback on:

**Content Effectiveness:**
- Purpose clarity and achievement
- Message structure and organization
- Key information completeness
- Call-to-action clarity
- Appropriate level of detail

**Professional Standards:**
- Tone appropriateness for recipient and context
- Professional language and etiquette
- Grammar, spelling, and punctuation
- Email formatting and structure
- Subject line effectiveness

**Communication Best Practices:**
- Recipient consideration and respect
- Cultural sensitivity and appropriateness
- Timing and urgency indicators
- Follow-up requirements
- Legal and compliance considerations

**Specific Areas I Evaluate:**
- Opening: Does it establish context quickly?
- Body: Is the message clear and well-organized?
- Closing: Does it specify next steps or expectations?
- Overall: Will this achieve the desired outcome?

I will provide specific, actionable feedback as bullet points for improvement.
    """,
    tools=[google_search],
    output_key="review_feedback"
)

email_polisher_agent = Agent(
    name="email_polisher_agent",
    model="gemini-2.0-flash", 
    description="Agent to create the final polished email based on review feedback.",
    instruction="""
I create the final, polished version of an email by incorporating review feedback and ensuring professional excellence.

**Original Email Draft:**
{email_draft}

**Review Feedback to Incorporate:**
{review_feedback}

I will produce:

**Final Polished Email:**
- Refined content addressing all feedback
- Professional formatting and structure
- Optimized subject line
- Clear call-to-action
- Appropriate tone and style
- Error-free grammar and spelling

**Quality Enhancements:**
- Improved clarity and conciseness
- Enhanced professional impact
- Better recipient engagement
- Stronger call-to-action
- Polished language and flow

**Email Components:**
- **Subject Line**: Clear, specific, and compelling
- **Greeting**: Appropriate for relationship and context
- **Opening**: Quick context establishment
- **Body**: Well-organized key points
- **Closing**: Clear next steps
- **Signature**: Professional sign-off

The final output will be a professional, ready-to-send email that effectively communicates the intended message while maintaining appropriate tone and professionalism.
    """,
    tools=[google_search],
    output_key="final_email"
)

email_pipeline_agent = SequentialAgent(
    name="EmailAssistantPipelineAgent",
    sub_agents=[
        email_drafter_agent,
        email_reviewer_agent, 
        email_polisher_agent
    ],
    description="Complete email creation pipeline: drafts, reviews, and polishes professional emails."
)

root_agent = email_pipeline_agent