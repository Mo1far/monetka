import os

from dotenv import load_dotenv

load_dotenv('.env')

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_HOST = os.environ.get('DB_HOST')
PORT = os.environ.get('PORT')
DB_NAME = os.environ.get('DB_NAME')
PASSWORD = os.environ.get('PASSWORD')
