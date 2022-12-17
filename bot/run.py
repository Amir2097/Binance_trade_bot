import time
import logging
import asyncio
import configparser
from aiogram import Bot, Dispatcher, executor, types
import requests

MSG = "Программировал ли ты сегодня, {}?"

logging.basicConfig(level=logging.INFO)
configpath = "configtelebot.conf"
config = configparser.ConfigParser()
config.read(configpath)
TOKEN = config['TOKEN']['access_token']

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    """
    Функция старта
    :param message:
    :return: Ответ бота
    """
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply(f"Привет, {user_full_name}!")



symbol = 'BTCUSDT'
level = 30000


@dp.message_handler(commands=["1"])
async def start_handler(message: types.Message):
    """

    :param message:
    :return:
    """
    url = 'https://fapi.binance.com/fapi/v1/trades?symbol=' + symbol + '&limit=' + '1'
    data = requests.get(url).json()
    price = data[-1]['price']

    if float(price) < level:
        text = symbol + ' : ' + price
        await message.reply(f"Торгуется, {text}!")

executor.start_polling(dp)


