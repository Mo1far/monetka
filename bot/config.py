import os

from dotenv import load_dotenv

load_dotenv('.env')

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
USERNAME = os.environ.get('USERNAME')
SERVER = os.environ.get('SERVER')
PORT = os.environ.get('PORT')
DB_NAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('USERNAME')