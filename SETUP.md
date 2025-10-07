# ADK1 Setup Guide

This guide will help you set up the AI Agent Development Kit (ADK1) on your local machine step-by-step.

## Prerequisites

Before you begin, make sure you have the following installed:
- **Python 3.8+** (check with `python --version` or `python3 --version`)
- **Git** (check with `git --version`)
- **A text editor or IDE** (VS Code, PyCharm, etc.)

## Step 1: Get Your Google API Key

You'll need a Google API key to use the Gemini AI models:

1. Visit the [Google AI Studio API Key page](https://ai.google.dev/gemini-api/docs/api-key)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy your API key and save it somewhere safe
5. Set up your API key as an environment variable:

   **On Linux/Mac:**
   ```bash
   export GOOGLE_API_KEY="your-api-key-here"
   ```
   
   **On Windows (Command Prompt):**
   ```cmd
   set GOOGLE_API_KEY=your-api-key-here
   ```
   
   **On Windows (PowerShell):**
   ```powershell
   $env:GOOGLE_API_KEY="your-api-key-here"
   ```

## Step 2: Clone the Repository

1. Open your terminal or command prompt
2. Navigate to where you want to store the project
3. Clone the repository:
   ```bash
   git clone https://github.com/michaelprosario/adk1
   ```
4. Navigate into the project directory:
   ```bash
   cd adk1
   ```

## Step 3: Set Up Python Environment

Creating a virtual environment keeps your project dependencies isolated:

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
   
2. Activate the virtual environment:
   
   **On Linux/Mac:**
   ```bash
   source .venv/bin/activate
   ```
   
   **On Windows:**
   ```cmd
   .venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Step 4: Verify Installation

Test that everything is working correctly:

1. Navigate to the agents directory:
   ```bash
   cd agents
   ```

2. Run the ADK web interface:
   ```bash
   adk web
   ```

3. Open your web browser and go to the URL shown in the terminal (usually `http://localhost:8080`)

## Next Steps

Once setup is complete, you can:
- Explore the available agents in the `agents/` directory
- Check the main `README.md` for detailed usage instructions
- Start with the Cover Letter Drafter agent as a beginner-friendly example

## Troubleshooting

**Common Issues:**

- **"python command not found"**: Try using `python3` instead of `python`
- **"pip command not found"**: Try using `pip3` instead of `pip`
- **API key errors**: Make sure your `GOOGLE_API_KEY` environment variable is set correctly
- **Permission errors**: On Linux/Mac, you might need to use `sudo` for some installations

