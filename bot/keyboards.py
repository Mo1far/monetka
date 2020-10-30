from aiogram.types import ReplyKeyboardRemove, \
     ReplyKeyboardMarkup, KeyboardButton, \
     InlineKeyboardMarkup, InlineKeyboardButton

menu = ReplyKeyboardMarkup(
     keyboard=[
         [
             KeyboardButton(text='Deposit'),
             KeyboardButton(text='Withdraw'),
             KeyboardButton(text='Balance')
         ],
         [
             KeyboardButton(text='Play'),
             KeyboardButton(text='Pooling')
         ],
         [
             KeyboardButton(text='Global pool info'),
             KeyboardButton(text='Help')
         ]
     ],
     resize_keyboard=True
 )