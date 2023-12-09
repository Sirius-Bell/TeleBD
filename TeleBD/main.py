#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.12

import asyncio

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.enums import ParseMode

from config import logger, config
from tg.handlers import router


async def main():
    bot = Bot(config.token.get_secret_value(), parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logger.info("Starting the bot...")
    asyncio.run(main())
