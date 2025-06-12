# AI Book Club Host

A modular Python chatbot for managing and automating book club activities, with AI-powered features.

## Features

- **Book Recommendations**: Get curated or AI-generated book suggestions.
- **Meeting Scheduling/Reminders**: Automate and notify book club events.
- **Discussion Prompts**: Generate questions to spark conversation.
- **Summaries**: Summarize chapters or discussions using AI.
- **Platform Integration**: Easily adaptable for Slack, Discord, or web.

## Usage

1. Clone the repo and install Python 3.8+.
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the bot:
   ```bash
   python main.py
   ```
4. In the demo CLI, type commands like:
   - `recommend AI`
   - `schedule Thursday 7pm`
   - `remind 1 hour before`
   - `prompt Life 3.0`
   - `summarize [paste chapter text]`

## Extending

- Implement AI-powered features in `discussion.py`.
- Add Slack/Discord/Web integration in `platform_adapter.py`.
- Expand book sources in `book_recommender.py`.
