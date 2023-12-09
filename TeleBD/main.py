#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.12

import asyncio
from config import logger, TOKEN
from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram import Dispatcher
from tg.handlers import router


async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logger.info("Starting the bot...")
    asyncio.run(main())
