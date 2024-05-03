import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging
from dotenv import load_dotenv
from os import getenv
import random

load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    print(message.from_user)
    await message.answer(f"Привет, {message.from_user.first_name}")


@dp.message(Command('info'))
async def my_info(message: types.Message):
    user = message.from_user
    await message.reply(
        f"Ваш ID: {user.id}\n"
        f"Имя: {user.first_name}\n"
        f"Username: {user.username}"
    )

# Здесь одни и те же фото не повторяются


# photos = [
#     "pic1.jpg",
#     "pic2.jpg",
#     "pic3.jpg",
#     "pic4.jpg",
#     "pic5.jpg"
# ]
# sent_photos = []


# @dp.message(Command("picture"))
# async def random_pic(message: types.Message):
#     if len(sent_photos) == len(photos):
#         sent_photos.clear()

#     random_image = random.choice([p for p in photos if p not in sent_photos])
#     sent_photos.append(random_image)
#     photo_path = f"images/{random_image}"
#     photo = types.FSInputFile(photo_path)
#     await message.reply_photo(photo)


@dp.message(Command("picture"))
async def random_pic(message: types.Message):
    photo = (
        "pic1.jpg",
        "pic2.jpg",
        "pic3.jpg",
        "pic4.jpg",
        "pic5.jpg"
    )
    random_image = random.choice(photo)
    photo_directory = f"images/{random_image}"
    photo = types.FSInputFile(photo_directory)
    await message.reply_photo(photo)


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
