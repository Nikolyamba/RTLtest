import asyncio
from bot.dispatcher import dp, bot
from aiogram.types import BotCommand

import bot.handlers

async def on_startup():
    commands = [
        BotCommand(command="/start", description="Start"),
        BotCommand(command="/help", description="Help"),
    ]
    await bot.set_my_commands(commands)

async def main():
    await on_startup()
    await dp.start_polling(bot, allowed_updates=["message"])
    await bot.delete_webhook(drop_pending_updates=True)

if __name__ == "__main__":
    asyncio.run(main())