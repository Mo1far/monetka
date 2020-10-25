from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.executor import Executor
from sqlalchemy import create_engine

from bot.config import TELEGRAM_BOT_TOKEN
from bot.config import USERNAME
from bot.config import SERVER
from bot.config import PORT
from bot.config import DB_NAME
from bot.config import PASSWORD

bot = Bot(token=TELEGRAM_BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot=bot, storage=MemoryStorage())
executor = Executor(dp, skip_updates=True)

engine = create_engine(f'posrgresql://{USERNAME}:{PASSWORD}@{SERVER}:{PORT}/{DB_NAME}')
