#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.12

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from loguru import logger

from tg.kb import menu

router = Router()


@router.message(CommandStart())
@router.message(F.text == "Меню")
async def start_handler(msg: Message):
    logger.info("Catch start command, handling...")
    await msg.answer("Что вы хотите сделать?", reply_markup=menu)


@router.callback_query(F.data == "add_option")
async def add_option_handler(callback: CallbackQuery):
    await callback.answer("HowToPoop")
