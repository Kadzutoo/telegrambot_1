import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values

token = dotenv_values(".env").get("BOT_TOKEN")
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f"Добро пожаловать, {name}!")

@dp.message(Command("myinfo"))
async def myinfo_handler(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    await message.answer(
        f"Ваш id: {user_id}\n"
        f"Ваше имя: {first_name}\n"
        f"Ваш username: @{username}"
    )


names = ["Арген", "Игорь", "Жоха", "Дмитрий", "Бермет", "Элдин", "Ажимура"]


@dp.message(Command("random"))
async def random_handler(message: types.Message):
        random_name = random.choice(names)
        await message.answer(f"Случайное имя: {random_name}")



async def echo_handler(message: types.Message):
    txt = message.text
    await message.answer(txt)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())