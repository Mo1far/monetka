from aiogram import types
from aiogram.types import User as TgUser
from bot.core import dp, bot, Session
from bot.models.user import User
from bot.models.token import Token
from bot.models.rounds_info import Round_info
from bot.models.wallet import Wallet
from bot.models.transaction import Transaction
from bot.models.transfer import  Transfer
from bot.models.game import Game
from bot.models.riskpool import Riskpool
from bot.models.token_riskpool import association_table
import bot.keyboards as kb

session = Session()

@dp.message_handler(commands='start')
async def cmd_start(msg: types.Message):
    tg_user = TgUser.get_current()

    result = session.query(User).filter(User.telegram_id==tg_user.id).first()
    if result is None:
        user = User(telegram_id=tg_user.id, username=tg_user.username)
        session.add(user)
        session.commit()
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
    tg_user = TgUser.get_current()
    tkn_in_wallet = session.query(User, Wallet, Token).select_from(User).join(Wallet).\
        join(Token).filter(User.telegram_id == tg_user.id).all()

    if (tkn_in_wallet is not None) and (len(tkn_in_wallet) > 0):
        for usr, wal, tok in tkn_in_wallet:
            await msg.answer("On Deposit")
            await msg.answer(f"{tok.token} --> {float(tok.balance)}")

        tkn_in_pool=session.query(User, Wallet, Token, Riskpool).select_from(User).join(Wallet).\
            join(Token).join(Riskpool).filter(User.telegram_id == tg_user.id
                                              and Riskpool.rp_id is not None).all()
        if (tkn_in_pool is not None) and (len(tkn_in_pool) > 0):
            for usr, wal, tok, pool in tkn_in_pool:
                await msg.answer("On riskpool")
                await msg.answer(f"{tok.token} --> {tok.balance}")
            else:
                msg.answer("В risk pool пока ничего нету")
    else:
        await msg.answer(f"Ой, {tg_user.username}, у тебя нету ни одного токена, пополни баласнс для начала")

@dp.message_handler(text="Play")
async def btn_cmd_help(msg: types.Message):
    await msg.answer(f'''Вы выбрали {msg.text}''')

@dp.message_handler(text="Pooling")
async def btn_cmd_help(msg: types.Message):
    await msg.answer(f'''Вы выбрали {msg.text}''')

@dp.message_handler(text="Global pool info")
async def btn_cmd_help(msg: types.Message):
    glb_pool = session.query(Token, Riskpool).select_from(Token.token).join(Riskpool).all()
    if (glb_pool is not None) and (len(glb_pool > 0)):
        for tk, rp in glb_pool:
           await msg.answer(f"{tk.token} --> {tk.balance}")
    await msg.answer(f'''Вы выбрали {msg.text}''')
