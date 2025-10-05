from google.adk.agents import Agent, LlmAgent, SequentialAgent
from google.adk.tools import google_search

resume_analyzer_agent = Agent(
    name="resume_analyzer_agent",
    model="gemini-2.0-flash",
    description="Agent to analyze a resume and identify areas for improvement.",
    instruction="""
I analyze resumes to identify strengths, weaknesses, and optimization opportunities.
Provide me with:
1. Current resume content
2. Target job role or industry (optional)

I will provide comprehensive analysis covering:

**Content Analysis:**
- Skills and experience assessment
- Achievement quantification opportunities
- Missing keywords for ATS optimization
- Industry-specific terminology gaps

**Structure Analysis:**
- Section organization and flow
- Length and formatting issues
- Contact information completeness
- Professional summary effectiveness

**ATS Optimization:**
- Keyword density analysis
- Format compatibility issues
- Section header optimization
- Parsing-friendly formatting

**Market Alignment:**
- Current industry trends
- Competitive positioning
- Skill gap identification
- Experience presentation optimization

**Key areas I examine:**
- Professional summary impact
- Work experience descriptions and metrics
- Skills section relevance and organization
- Education and certifications positioning
- Overall narrative consistency
- ATS compatibility and keyword optimization
    """,
    tools=[google_search],
    output_key="resume_analysis"
)

resume_optimizer_agent = Agent(
    name="resume_optimizer_agent", 
    model="gemini-2.0-flash",
    description="Agent to optimize resume content based on analysis feedback.",
    instruction="""
I optimize resume content based on detailed analysis to improve impact and ATS compatibility.

**Resume Analysis to Address:**
{resume_analysis}

I will enhance the resume by:

**Content Optimization:**
- Rewriting bullet points for maximum impact
- Adding quantifiable achievements and metrics
- Incorporating relevant industry keywords
- Improving action verb usage and variety

**Structure Enhancement:**
- Reorganizing sections for optimal flow
- Optimizing section headers for ATS parsing
- Ensuring consistent formatting
- Improving readability and scan-ability

**ATS Compatibility:**
- Integrating essential keywords naturally
- Using standard section names
- Ensuring proper formatting for parsing
- Maintaining clean, simple structure

**Professional Positioning:**
- Strengthening professional summary
- Highlighting transferable skills
- Emphasizing career progression
- Aligning with target role requirements

I will provide specific, actionable improvements with before/after examples where helpful.
My recommendations will be organized by section for easy implementation.
    """,
    tools=[google_search],
    output_key="optimization_recommendations"
)

resume_formatter_agent = Agent(
    name="resume_formatter_agent",
    model="gemini-2.0-flash", 
    description="Agent to create the final optimized resume with professional formatting.",
    instruction="""
I create the final, professionally formatted resume incorporating all analysis and optimization recommendations.

**Original Resume Analysis:**
{resume_analysis}

**Optimization Recommendations:**
{optimization_recommendations}

I will produce:

**Final Optimized Resume:**
- Clean, professional formatting
- ATS-compatible structure
- Optimized content with impact metrics
- Industry-appropriate keywords
- Consistent styling and layout
- Proper section organization

**Formatting Standards:**
- Professional fonts and spacing
- Consistent bullet point style
- Appropriate section headers
- Clean layout with good white space
- Contact information prominently displayed
- Easy-to-scan format for both humans and ATS

**Quality Assurance:**
- Grammar and spelling accuracy
- Consistent verb tenses
- Logical flow and progression
- Professional tone throughout
- Appropriate length (1-2 pages)

The final output will be a polished, job-ready resume in a clean format that effectively showcases the candidate's qualifications while being optimized for both ATS systems and human reviewers.
    """,
    tools=[google_search],
    output_key="final_resume"
)

resume_pipeline_agent = SequentialAgent(
    name="ResumeOptimizerPipelineAgent",
    sub_agents=[
        resume_analyzer_agent,
        resume_optimizer_agent, 
        resume_formatter_agent
    ],
    description="Complete resume optimization pipeline: analyzes, optimizes, and formats resumes for maximum impact."
)

root_agent = resume_pipeline_agent