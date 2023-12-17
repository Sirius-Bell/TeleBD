#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.12

import asyncio
import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from loguru import logger
from pydantic import SecretStr, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """ Project settings """
    token: SecretStr
    host: SecretStr
    port: SecretStr
    user: SecretStr
    password: SecretStr
    database_name: SecretStr

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')


LEVEL: str = "DEBUG"
SEPARATOR: str = ";"

logger.remove()
logger.add(os.path.join("logs", "log.log"),
           format="[{time:YYYY-MM-DD at HH:mm:ss}] [{level}]: {message}",
           level=LEVEL, retention="10 days")
logger.add(sys.stderr,
           format="<green>[{time:YYYY-MM-DD at HH:mm:ss}]</green> <cyan>[{level}]</cyan>: "
                  "<level>{message}</level>",
           level=LEVEL, colorize=True)

config = Settings()
loop = asyncio.get_event_loop()

bot = Bot(config.token.get_secret_value(), parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage(), loop=loop)
