from bot.core import executor
from bot import handlers
def start():
    executor.start_polling()


if __name__ == '__main__':
    start()
