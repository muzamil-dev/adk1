# Cover Letter Drafter Agent

A sophisticated AI agent system for creating professional cover letters tailored to specific job opportunities.

## Overview

This system implements a three-stage pipeline for cover letter creation:

1. **Drafter Agent**: Creates an initial personalized cover letter
2. **Reviewer Agent**: Reviews the draft against best practices
3. **Editor Agent**: Produces the final polished version

## Features

- **Personalized Content**: Tailors letters to specific jobs and companies
- **Best Practice Validation**: Ensures professional standards are met
- **Company Research**: Uses Google Search to gather relevant company information
- **Professional Formatting**: Follows standard business letter format
- **Quality Assurance**: Multi-stage review process for optimal results

## Files

- `agent.py` - Main agent definitions and pipeline
- `prompt.md` - System requirements and documentation
- `run_cover_letter.py` - Simple runner script
- `test_scenarios.py` - Comprehensive test scenarios
- `README.md` - This file

## Usage

### Basic Usage
```bash
cd /workspaces/adk1/agents/cover_letter_drafter
python run_cover_letter.py
```

### Test Multiple Scenarios
```bash
python test_scenarios.py
```

### Integration in Other Code
```python
from agents.cover_letter_drafter.agent import root_agent

# Use root_agent (CoverLetterPipelineAgent) in your Runner
runner = Runner(agent=root_agent, ...)
```

## Input Requirements

When using the system, provide:

1. **Resume Background**: Your experience, skills, education, achievements
2. **Job Opportunity**: Position details, company info, requirements

## Output

The system produces a professional cover letter that:
- Addresses the specific position and company
- Highlights relevant experience and skills
- Demonstrates company knowledge and fit
- Uses professional language and formatting
- Is ready for submission

## Architecture

The system uses Google's Agent Development Kit (ADK) with:
- **Sequential Agent Pattern**: Processes requests through multiple specialized agents
- **Tool Integration**: Google Search for company research
- **Memory Management**: Passes data between agents in the pipeline
- **Async Processing**: Non-blocking execution for better performance

## Dependencies

- `google-adk`
- `google-generativeai`
- `asyncio`

## Examples

See `test_scenarios.py` for examples of different job types:
- Software Engineer positions
- Marketing Manager roles
- Data Analyst positions
- And more...

Each scenario demonstrates how the system adapts to different industries and experience levels.

