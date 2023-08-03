from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kbCommands = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyBtn1= KeyboardButton('Help')
keyBtn2= KeyboardButton('About')
keyBtn3= KeyboardButton('Subscriptions')
keyBtn4= KeyboardButton('Adresses')
kbCommands.add(keyBtn1,keyBtn2,keyBtn3,keyBtn4)

ikbSubscriptions = InlineKeyboardMarkup(row_width = 1)
inKeyBtn1= InlineKeyboardButton(text = 'Tier 1 🤑', callback_data= "Tier 1")
inKeyBtn2= InlineKeyboardButton(text = 'Tier 2 💵', callback_data= "Tier 2")
inKeyBtn3= InlineKeyboardButton(text = 'Tier 3 🚀💸', callback_data= "Tier 3")
ikbSubscriptions.add(inKeyBtn1).add(inKeyBtn2).add(inKeyBtn3)

ikbFAQ = InlineKeyboardMarkup(row_width = 2)
inBtnAgree = InlineKeyboardButton(text = 'Agree✅ ', callback_data= "Agree")
inBtnDissagree = InlineKeyboardButton(text = 'Disagree❌ ', callback_data= "Disagree")
ikbFAQ.add(inBtnAgree).add(inBtnDissagree)
