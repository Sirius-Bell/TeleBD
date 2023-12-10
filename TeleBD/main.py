#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.12

import asyncio
from typing import NoReturn

from config import logger, bot, dp
from TeleBD.tg.routers.handler_options import router
from TeleBD.tg.routers.common import common_router


async def main() -> NoReturn:
    dp.include_router(common_router)
    dp.include_router(router)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logger.info("Starting the bot...")
    asyncio.run(main())
