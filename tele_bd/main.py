#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.12

from typing import NoReturn

from tele_bd.config import logger, bot, dp, loop
from tele_bd.tg.routers.handler_options import router
from tele_bd.tg.routers.common import common_router


async def main() -> NoReturn:
    """
    Main function, includes all routers and starts polling
    :return: None
    :rtype: NoReturn
    """
    dp.include_router(common_router)
    dp.include_router(router)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logger.info("Starting the bot...")
    loop.run_until_complete(main())
