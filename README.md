# Chatbot Implementation using Telegram

This project implements a Telegram chatbot using Python, OpenAI's GPT-3.5, and Telegram's Bot API.

## Project Overview

The goal of this project is to create a chatbot that can interact with users on Telegram using natural language processing capabilities provided by OpenAI's GPT-3.5 model. The chatbot will respond to user queries, provide information, and perform basic conversational tasks.

## Features

- **Welcome Message**: Sends a welcome message when the user starts the chat.
- **Command Handling**: Responds to commands like `/start`, `/help`, and `/clear`.
- **Interactive Conversations**: Engages in interactive conversations with users based on their inputs.
- **Memory Channel**: Remembers the context of the conversation for a short period using a memory channel.
- **Chat Completion**: Uses OpenAI's GPT-3.5 model for generating responses to user queries.
- **Deployment**: Deploys the chatbot to Telegram using Telegram's Bot API.

## Installation

1. **Clone the repository:**

   ```bash
   git clone "https://github.com/sahiltambe/Chatbot-Implementation-using-Telegram"
   cd Chatbot-Implementation-using-Telegram

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt

3. **Set up environment variables:**

    Create a .env file in the project root and add the following:
    TELEGRAM_BOT_TOKEN=<your_telegram_bot_token>
    OPENAI_API_KEY=<your_openai_api_key>


## Setup Instructions

### Prerequisites

- Python 3.7 or higher installed
- Telegram account
- OpenAI API key

### Telegram Bot Setup

1. **Create a Telegram Bot**
   - Open Telegram and search for "BotFather" (channel with blue tick).
   - Start a chat with BotFather and create a new bot by sending `/newbot`.
   - Give your bot a specific name ending in "_bot", for example, "/yourbotname_bot".
   - Copy the HTTP API token provided by BotFather and paste it into your `.env` file:
     ```
     TELEGRAM_BOT_TOKEN="your_telegram_HTTP_API"
     ```
   - Open the link provided by BotFather in the same message, which looks like `t.me/yourbotname_bot`.

2. **Run the Chatbot**
   - Execute `Telegram_chatbot.py` in your command prompt:
     ```
     python Telegram_chatbot.py
     ```
   - Start chatting with your Telegram bot.

### Running the Chatbot

- The chatbot will respond to various prompts and engage in natural conversations based on the messages received.


## Interact with the bot on Telegram:

Open Telegram and start a conversation with your bot. Use commands like /start, /help, and ask questions to engage in conversation.

Bot Commands
/start: Initiates the conversation with a welcome message.
/help: Displays the list of available commands.
/clear: Clears the conversation history.
Contributing
Contributions are welcome! If you have suggestions or improvements, please fork the repository and create a pull request.

## Dependencies

- `python-telegram-bot`
- `openai`

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## Contact
For any questions or support, please contact [sahiltambe1996@gmail.com](mailto:sahiltambe1996@gmail.com).