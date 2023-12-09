#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.12


import os
import sys

from dotenv import load_dotenv
from loguru import logger
from db_connect import DatabaseConnect

load_dotenv()

HOST: str = os.getenv('HOST')
PORT: int = int(os.getenv('PORT'))
USER: str = os.getenv('USER')
PASSWORD: str = os.getenv('PASSWORD')
DATABASE: str = os.getenv('DATABASE_NAME')
TOKEN: str = os.getenv('TOKEN')

LEVEL: str = "DEBUG"

logger.remove()
logger.add(os.path.join("logs", "log.log"), format="[{time:YYYY-MM-DD at HH:mm:ss}] [{level}]: {message}",
           level=LEVEL, retention="10 days")
logger.add(sys.stderr,
           format="<green>[{time:YYYY-MM-DD at HH:mm:ss}]</green> <cyan>[{level}]</cyan>: <level>{message}</level>",
           level=LEVEL, colorize=True)

db = DatabaseConnect(HOST, PORT, USER, PASSWORD, DATABASE)
