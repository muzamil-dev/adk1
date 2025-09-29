# ADK1 - AI Agent Development Kit Examples

A collection of AI agents built using Google's Agent Development Kit (ADK) for various automation tasks.

## Setup Environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Get Your Google API Key

You'll need a Google API key to use the Gemini AI models:

1. Visit the [Google AI Studio API Key page](https://ai.google.dev/gemini-api/docs/api-key)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy your API key and save it somewhere safe

### Setup environment variables

### Linux/Mac

``` bash
export GOOGLE_GENAI_USE_VERTEXAI=FALSE
export GOOGLE_API_KEY=FIXME
export GEMINI_API_KEY=fix
```

### Windows

**Command Prompt:**
``` cmd
set GOOGLE_GENAI_USE_VERTEXAI=FALSE
set GOOGLE_API_KEY=FIXME
set GEMINI_API_KEY=fix
```

**PowerShell:**
``` powershell
$env:GOOGLE_GENAI_USE_VERTEXAI="FALSE"
$env:GOOGLE_API_KEY="FIXME"
$env:GEMINI_API_KEY="fix"
```



## Available Agents

### 1. Cover Letter Drafter (`agents/cover_letter_drafter/`)
**Three-stage pipeline for creating professional cover letters**

- **Drafter Agent**: Creates personalized cover letter drafts
- **Reviewer Agent**: Reviews drafts against best practices  
- **Editor Agent**: Produces final polished versions

**Features:**
- Tailored to specific job opportunities
- Company research integration
- Professional formatting
- Quality assurance through multi-stage review

**Usage:**
```bash
cd agents/cover_letter_drafter
python run_cover_letter.py           # Simple example
python test_scenarios.py             # Multiple test scenarios
```

### 2. Blogger (`agents/blogger/`)
**Multi-agent blog writing and editing pipeline**

- Content creation and revision workflow
- Quality review and feedback system
- SEO and engagement optimization

### 3. Code and Review (`agents/code_and_review/`)
**Code generation and review automation**

### 4. Multi-Tool Agent (`agents/multi_tool_agent/`)
**General-purpose agent with multiple tool integrations**

### 5. Spock Agent (`agents/spock_agent/`)
**Star Trek Spock personality agent**

## Project Structure

```
├── agent_runner/              # Main execution scripts
│   ├── main.py               # Memory example runner
│   └── cover_letter_integration_example.py
├── agents/                   # Agent definitions
│   ├── cover_letter_drafter/ # Cover letter creation pipeline
│   ├── blogger/             # Blog writing pipeline  
│   ├── code_and_review/     # Code review agents
│   ├── multi_tool_agent/    # Multi-purpose agent
│   └── spock_agent/         # Personality agent
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Key Dependencies

- `google-adk` - Google Agent Development Kit
- `google-generativeai` - Google Gemini AI models
- `asyncio` - Asynchronous programming support


