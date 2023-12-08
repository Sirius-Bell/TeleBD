#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.12

import asyncio
import aiomysql
from config import logger
from asyncio import AbstractEventLoop


class DatabaseConnect:

    def __init__(self, host: str, port: int, user: str, password: str, db_name: str,
                 loop: AbstractEventLoop = asyncio.get_event_loop()) -> None:
        """
        Class needed for connecting to database
        :param host: Host for connection
        :param port: Port for connection
        :param user: User for connection
        :param password: Password for connection
        :param loop: Event loop from main
        :return: None
        """
        self.connect = None
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db_name = db_name
        self.loop = loop

    async def connect(self):
        self.connect = await aiomysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                              db=self.db_name, loop=self.loop)
        logger.debug(f"Connection: {self.connect}")

        await self.connect.cursor()
