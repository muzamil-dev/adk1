# Cover Letter Drafter Agent System

## Overview
A three-stage pipeline for creating professional cover letters tailored to specific job opportunities.

## User Requirements

**Given:**
- Resume background/experience information
- Job opportunity details (link or description)

**When:**
- The agent pipeline executes

**Then:**
- **Stage 1 (Drafter):** Creates initial cover letter draft
- **Stage 2 (Reviewer):** Reviews draft against best practices
- **Stage 3 (Editor):** Produces final polished cover letter

## Agent Pipeline

### 1. Cover Letter Drafter Agent
- **Purpose:** Creates initial personalized cover letter
- **Input:** Resume background + job opportunity details
- **Output:** Professional cover letter draft
- **Features:**
  - Tailored to specific job requirements
  - Highlights relevant experience
  - Demonstrates company knowledge
  - Follows standard business letter format

### 2. Cover Letter Reviewer Agent
- **Purpose:** Quality assurance and best practice validation
- **Input:** Cover letter draft
- **Output:** Detailed review feedback
- **Evaluation Criteria:**
  - Structure and formatting
  - Content relevance and quality
  - Professional writing style
  - Grammar and clarity

### 3. Cover Letter Editor Agent
- **Purpose:** Final polish and refinement
- **Input:** Original draft + review feedback
- **Output:** Job-ready final cover letter
- **Features:**
  - Incorporates all feedback
  - Maintains professional tone
  - Ensures proper formatting
  - Optimizes for impact

## Usage Example
```
Input: 
- "I have 5 years of software engineering experience with Python and React..."
- "Job posting: Senior Frontend Developer at TechCorp..."

Output:
- Professional cover letter specifically crafted for the TechCorp position
```

## Implementation Notes
- Based on the blogger agent pattern from `agents/blogger/`
- Uses SequentialAgent for pipeline execution
- Includes Google search tool for company research
- Each agent has specific output keys for data flow
