#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.12


import os
import sys

from loguru import logger
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    token: SecretStr
    host: SecretStr
    port: SecretStr
    user: SecretStr
    password: SecretStr
    database_name: SecretStr

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


LEVEL: str = "DEBUG"

logger.remove()
logger.add(os.path.join("logs", "log.log"), format="[{time:YYYY-MM-DD at HH:mm:ss}] [{level}]: {message}",
           level=LEVEL, retention="10 days")
logger.add(sys.stderr,
           format="<green>[{time:YYYY-MM-DD at HH:mm:ss}]</green> <cyan>[{level}]</cyan>: <level>{message}</level>",
           level=LEVEL, colorize=True)

config = Settings()
