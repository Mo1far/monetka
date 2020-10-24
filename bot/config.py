import os

from dotenv import load_dotenv

load_dotenv('.env')

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
