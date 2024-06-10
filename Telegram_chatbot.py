# Importing necessary libraries and modules
from aiogram import Bot, Dispatcher, executor, types  # Telegram bot API
from dotenv import load_dotenv  # For loading environment variables
import os  # For interacting with the operating system
import logging  # For logging information
import openai  # For interacting with OpenAI API

# Load environment variables from .env file
load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Telegram bot token
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # OpenAI API key

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

# Define the model name to be used with OpenAI
MODEL_NAME = "gpt-3.5-turbo"

# Initialize the Telegram bot
bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot)  # Initialize the dispatcher

# Define a class to hold the bot's response
class Reference:
    def __init__(self) -> None:
        self.response = ""  # Initialize with an empty response

# Create an instance of the Reference class
reference = Reference()

# Function to clear the past response
def clear_past():
    reference.response = ""

# Handler for the /start command
@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    This handler receives messages with `/start` command and sends a welcome message.
    
    Args:
        message (types.Message): Incoming message object
    """
    await message.reply("Hi\nI am a Chat Bot! Created by Sahil. How can I assist you?")

# Handler for the /help command
@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    A handler to display the help menu.
    
    Args:
        message (types.Message): Incoming message object
    """
    help_command = """
    Hello! I am a chatbot developed by Sahil. Here are some commands you can use:
    /start - to initiate a conversation with me.
    /clear - to reset our previous conversation and context.
    /help - to display this help menu with available commands.
    
    Feel free to ask me anything, and I'll do my best to assist you!
    """
    await message.reply(help_command)

# Handler for the /clear command
@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    A handler to clear the previous conversation and context.
    
    Args:
        message (types.Message): Incoming message object
    """
    clear_past()  # Clear the past response
    await message.reply("I've cleared the past conversation and context.")

# Handler for processing user messages
@dispatcher.message_handler()
async def main_bot(message: types.Message):
    """
    A handler to process the user's input and generate a response using the OpenAI API.
    
    Args:
        message (types.Message): Incoming message object
    """
    print(f">>> USER: \n\t{message.text}")  # Print user's message

    # Generate a response using OpenAI's ChatCompletion
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[
            {"role": "assistant", "content": reference.response},  # Previous assistant response
            {"role": "user", "content": message.text}  # User's input
        ]
    )
    
    # Update the reference response with the new response from OpenAI
    reference.response = response['choices'][0]['message']['content']
    print(f">>> chatGPT: \n\t{reference.response}")  # Print the bot's response
    await bot.send_message(chat_id=message.chat.id, text=reference.response)  # Send the response to the user

# Entry point of the script
if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)  # Start polling for new updates
