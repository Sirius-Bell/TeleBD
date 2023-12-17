#!/usr/bin/env python
# -*- coding: utf8 -*-
from typing import NoReturn

# ---Sirius Bell---
# Python 3.12


from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.types import Message, CallbackQuery
from loguru import logger
from tele_bd.config import config
from tele_bd.database.db import db

common_router = Router()
db_name = config.database_name.get_secret_value()


@common_router.message(CommandStart())
async def start_handler(msg: Message, state: FSMContext) -> NoReturn:
    """
    Start handler, welcome users
    :ivar msg: message from user
    :vartype msg: Message
    :ivar state: state user
    :vartype state: FSMContext
    :return: None
    :rtype: NoReturn
    """
    await state.clear()
    builder = InlineKeyboardBuilder()
    for i in await db.execute(f"SHOW TABLES FROM {db_name}"):
        builder.add(
            InlineKeyboardButton(text=i[f'Tables_in_{db_name}'],
                                 callback_data=f"table_{i[f'Tables_in_{db_name}']}"))
    await msg.answer(text="Выберите таблицу:", reply_markup=builder.as_markup())


@common_router.message(StateFilter(None), Command(commands=["cancel"]))
@common_router.message(default_state, F.text.lower() == "отмена")
async def cmd_cancel_not(msg: Message, state: FSMContext) -> NoReturn:
    """
    Handler to cancel nothing
    :ivar msg: message from user
    :vartype msg: Message
    :ivar state: state user
    :vartype state: FSMContext
    :return: None
    :rtype: NoReturn
    """
    logger.info("Clearing the data from states")
    await state.set_data({})
    await msg.answer("Отменять нечего.")


@common_router.message(Command(commands=["cancel"]))
@common_router.message(F.text.lower() == "отмена")
@common_router.callback_query(F.data == "cancel_")
async def cmd_cancel(callback: CallbackQuery, state: FSMContext) -> NoReturn:
    """
    Handler to cancel operation
    :ivar callback: callback from inline button
    :vartype callback: CallbackQuery
    :ivar state: state user
    :vartype state: FSMContext
    :return: None
    :rtype: NoReturn
    """
    await state.clear()
    await callback.answer(text="Действие отменено")
