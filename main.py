import logging

from openai_helper import OpenAIHelper
from telegram_bot import ChatGPT3TelegramBot

OPENAI_API_KEY = "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"
TELEGRAM_BOT_TOKEN = "6186372028:AAEa8PgCniHyHgJIo6B34PtilLlOV6gej4Q"
ALLOWED_TELEGRAM_USER_IDS = "*"


def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    openai_config = {
        'api_key': OPENAI_API_KEY,
        'show_usage': False,
        'max_history_size': 10,
        'max_conversation_age_minutes': 180,
        'assistant_prompt': 'You are a helpful assistant.',
        'max_tokens': 1200,
        'model': 'gpt-3.5-turbo',
        'temperature': 1,
        'n_choices': 1,
        'presence_penalty': 0,
        'frequency_penalty': 0,
    }

    telegram_config = {
        'token': TELEGRAM_BOT_TOKEN,
        'allowed_user_ids': ALLOWED_TELEGRAM_USER_IDS,
    }

    # Setup and run ChatGPT and Telegram bot
    openai_helper = OpenAIHelper(config=openai_config)
    telegram_bot = ChatGPT3TelegramBot(config=telegram_config, openai=openai_helper)
    telegram_bot.run()


if __name__ == '__main__':
    main()
