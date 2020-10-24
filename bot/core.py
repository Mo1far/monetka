from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.executor import Executor

from bot.config import TELEGRAM_BOT_TOKEN

bot = Bot(token=TELEGRAM_BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot=bot, storage=MemoryStorage())
executor = Executor(dp, skip_updates=True)
