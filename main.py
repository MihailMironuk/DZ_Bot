from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging
from dotenv import load_dotenv
from os import getenv
import random

from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    print(message.from_user)
    await message.answer(f"Привет, {message.from_user.first_name}")


@dp.message(commands=['myinfo'])
async def myinfo(message: types.Message):
    user = message.from_user
    await message.reply(
        f"Ваш ID: {user.id}\n"
        f"Имя: {user.first_name}\n"
        f"Username: {user.username}"
    )


@dp.message(Command("picture"))
async def send_picture(message: types.Message):
    photo = types.FSInputFile("2626328730.jpg","191006152638-01-pets-and-our-health.jpg")
    await message.answer_photo(
        photo=photo,
        caption="Котик 🐱"
    )

@dp.message()
async def echo(message: types.Message):
    # print(message)
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
