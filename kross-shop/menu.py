from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_menu(bot: Bot):
    menu = [
        BotCommand(
            command='/start',
            description='Запуск бота'
        ),



    ]
    await bot.set_my_commands(menu, BotCommandScopeDefault())
