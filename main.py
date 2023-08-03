from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from bs4 import BeautifulSoup
import aiohttp
import ssl
from config import TOKEN_API
from keyBoards import kbCommands, ikbSubscriptions, ikbFAQ
from text import ABOUT_TIERS_COMMAND ,FAQ_COMMAND , HELP_COMMAND, ABOUT_COMMAND

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id,
                           text = 'Welcome to Crypto Checker',
                           reply_markup = kbCommands)
    await message.delete()


@dp.message_handler(Text(equals = "Subscriptions"))
async def subscriptions_command(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id,
                           text = ABOUT_TIERS_COMMAND, parse_mode='HTML',
                           reply_markup = ikbSubscriptions)
    
@dp.message_handler(Text(equals = "Help"))
async def help_command(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id,
                           text = HELP_COMMAND, parse_mode='HTML')

@dp.message_handler(Text(equals = "About"))
async def about_command(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id,
                           text = ABOUT_COMMAND, parse_mode='HTML')

@dp.message_handler(Text(equals = "Adresses"))
async def help_command(message: types.Message):
    await message.answer(text="Send addresses")
    dp.register_message_handler(addresses_comp, content_types=types.ContentTypes.TEXT)

async def fetch_page(url):
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        async with session.get(url) as response:
            return await response.text()

async def addresses_comp(message: types.Message):
    addresses = message.text + "\n"
    with open('addresses.txt', 'w') as file_loc:
        file_loc.writelines(addresses)

    money = []
    with open('addresses.txt', 'r') as file_loc:
        addresses = file_loc.readlines()

    for addres in addresses:
        url = f"https://etherscan.io/address/{addres[:-1]}"
        response_after_search = await fetch_page(url)

        soup_after_search = BeautifulSoup(response_after_search, 'html.parser')
        info_div = soup_after_search.find_all('h4', {'class': 'text-cap mb-1'})
        value = info_div[1].parent
        value = str(value)

        numb = 50
        money_count = []
        while value[numb:]:
            if value[numb] == '.':
                break

            money_count.append(value[numb])
            numb += 1

        money.append("".join(money_count))

    with open('money.txt', 'w') as file_loc:
        file_loc.writelines("\n".join(money))

    with open('addresses.txt', 'r') as file_loc:
        addresses = file_loc.readlines()

    with open('money.txt', 'r') as file_loc:
        money_list = file_loc.readlines()

    answer = ""
    for address, money_c in zip(addresses, money_list):
        answer += address + " - " + money_c + "\n"

    await message.answer(text=answer)



@dp.callback_query_handler(text = 'Tier 1')
async def tierFirst_callback(callback: types.CallbackQuery):
    await callback.message.answer(FAQ_COMMAND, parse_mode='HTML', reply_markup = ikbFAQ)

@dp.callback_query_handler(text = 'Tier 2')
async def tierSecond_callback(callback: types.CallbackQuery):
    await callback.message.answer(FAQ_COMMAND, parse_mode='HTML', reply_markup = ikbFAQ)

@dp.callback_query_handler(text = 'Tier 3')
async def tierThird_callback(callback: types.CallbackQuery):
    await callback.message.answer(FAQ_COMMAND, parse_mode='HTML', reply_markup = ikbFAQ)

@dp.callback_query_handler(text = 'Agree')
async def Agree_callback(callback: types.CallbackQuery):
    await callback.answer("Payment")

@dp.callback_query_handler(text = 'Disagree')
async def Disagree_callback(callback: types.CallbackQuery):
    await callback.answer("You should accept our rules before using our bot")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)