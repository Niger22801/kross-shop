import asyncio
import logging
from aiogram import Bot, Dispatcher
from menu import set_menu
from aiogram.client.session.aiohttp import AiohttpSession


logging.basicConfig(level=logging.INFO)
TOKEN = 'ТОКЕН'
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()

async def main():
    await set_menu(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    from handlers import dp
    asyncio.run(main())
