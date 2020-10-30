from aiogram import types
from aiogram.types import User as TgUser
from bot.core import dp, bot, Session
from bot.models.user import User
import bot.keyboards as kb

session = Session()

@dp.message_handler(commands='start')
async def cmd_start(msg: types.Message):
    tg_user = TgUser.get_current()
    id = tg_user.id
    user = User()
    result = session.query(user).filter_by(user.telegram_id == 1010101010).first()
    await msg.answer(f'''Congrats {tg_user.username}!
Use the drawer below to check your balance, deposit/withdraw, play, or fund liquidity pools!
Want to start using your coins? Check the global liquidity pool, create your own or 
add liquidity to an existing pool, start betting!
For a quicktutorial use the "❓ Help" button or click /help''', reply_markup=kb.menu)


@dp.message_handler(commands='help')
async def cmd_help(msg: types.Message):
    await msg.answer(f'''Some text and links''')

@dp.message_handler(commands='menu')
async def show_menu(msg: types.Message):
    await msg.answer('Вы в главном меню', reply_markup=kb.menu)

@dp.message_handler(text="Help")
async def btn_cmd_help(msg: types.Message):
    await msg.answer(f'''Some text and links''')

@dp.message_handler(text="Deposit")
async def btn_cmd_help(msg: types.Message):
    await msg.answer(f'''Вы выбрали {msg.text}''')

@dp.message_handler(text="Withdraw")
async def btn_cmd_help(msg: types.Message):
    await msg.answer(f'''Вы выбрали {msg.text}''')

@dp.message_handler(text="Balance")
async def btn_cmd_help(msg: types.Message):
    await msg.answer(f'''Вы выбрали {msg.text}''')

@dp.message_handler(text="Play")
async def btn_cmd_help(msg: types.Message):
    await msg.answer(f'''Вы выбрали {msg.text}''')

@dp.message_handler(text="Pooling")
async def btn_cmd_help(msg: types.Message):
    await msg.answer(f'''Вы выбрали {msg.text}''')

@dp.message_handler(text="Global pool info")
async def btn_cmd_help(msg: types.Message):
    await msg.answer(f'''Вы выбрали {msg.text}''')
