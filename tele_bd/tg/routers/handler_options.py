#!/usr/bin/env python
# -*- coding: utf8 -*-
from typing import NoReturn

# ---Sirius Bell---
# Python 3.12

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from loguru import logger

from tele_bd.config import config, SEPARATOR
from tele_bd.tg.states.state_add import AddOption, DeleteOption
from tele_bd.tg.keyboards.kb import cancel, menu_opt
from tele_bd.database.db import db

router = Router()
db_name = config.database_name.get_secret_value()


@router.callback_query(F.data.startswith("table_"))
async def get_options_handler(callback: CallbackQuery, state: FSMContext) -> NoReturn:
    """
    Handler to get options with table
    :ivar callback: callback from inline button
    :vartype callback: CallbackQuery
    :ivar state: state user
    :vartype state: FSMContext
    :return: None
    :rtype: NoReturn
    """
    await state.set_data({})
    logger.info("Catch table callback")
    table_name = callback.data.lstrip("table_")
    rows = [i["Field"] for i in await db.execute(f"show COLUMNS from {table_name} from {db_name}")]
    id_t = await db.execute(f"SELECT {rows[0]} FROM {table_name}")
    id_t = str(id_t[-1][rows[0]] + 1)
    await state.set_data({"id_t": id_t, "rows": rows, "table_name": table_name})
    await callback.message.answer(text="Что вам нужно сделать с таблицей?", reply_markup=menu_opt)
    await callback.answer()


@router.callback_query(F.data == "add_option")
async def add_option_handler(callback: CallbackQuery, state: FSMContext) -> NoReturn:
    """
    Handler to catch state add data to table
    :ivar callback: callback from inline button
    :vartype callback: CallbackQuery
    :ivar state: state user
    :vartype state: FSMContext
    :return: None
    :rtype: NoReturn
    """
    logger.info("Catch add callback")
    await state.set_state(AddOption.add_rows)
    mess = f"Введите данные для всех столбцов, разделяя столбцы {SEPARATOR}, по такому образцу:\n\n{SEPARATOR.join((await state.get_data())['rows'][1:])}"
    await callback.message.answer(text=mess, reply_markup=cancel)
    await callback.answer(text="")


@router.message(AddOption.add_rows)
async def add_rows(msg: Message, state: FSMContext) -> NoReturn:
    """
    Handler to add data to table
    :ivar msg: message from user
    :vartype msg: Message
    :ivar state: state user
    :vartype state: FSMContext
    :return: None
    :rtype: NoReturn
    """
    state_data = await state.get_data()
    data = [state_data["id_t"]]
    data += msg.text.split(SEPARATOR)
    data = [int(s) if s.isdigit() else s for s in data]
    logger.debug(data)
    await db.add_data(table_name=state_data["table_name"], data=tuple(data))
    await msg.answer("Добавляем данные в базу...")


@router.callback_query(F.data == "all_options")
async def get_all_options(callback: CallbackQuery) -> NoReturn:
    """
    Handler to get all options with table
    :ivar callback: callback from inline button
    :vartype callback: CallbackQuery
    :return: None
    :rtype: NoReturn
    """
    await callback.message.answer(await db.get_all(table="services"), parse_mode="")
    await callback.answer()


@router.callback_query(F.data == "delete_option")
async def delete_option_first(callback: CallbackQuery, state: FSMContext) -> NoReturn:
    """
    Handler to catch state delete option
    :ivar callback: callback from inline button
    :vartype callback: CallbackQuery
    :ivar state: state user
    :vartype state: FSMContext
    :return: None
    :rtype: NoReturn
    """
    await callback.message.answer("Введите id, который нужно удалить:", reply_markup=cancel)
    await state.set_state(DeleteOption.delete_state)
    await callback.answer()


@router.message(DeleteOption.delete_state)
async def delete_option_second(msg: Message, state: FSMContext) -> NoReturn:
    """
    Handler to delete data from table
    :ivar msg: message from user
    :vartype msg: Message
    :ivar state: state user
    :vartype state: FSMContext
    :return: None
    :rtype: NoReturn
    """
    await msg.answer("Удаляем.")
    data = await state.get_data()
    logger.debug(data)
    await db.delete_data(data["table_name"], data["rows"][0], int(msg.text))
