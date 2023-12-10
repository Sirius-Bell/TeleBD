#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.12


from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, CallbackQuery
from tg.keyboards.kb import menu
from loguru import logger

common_router = Router()


@common_router.message(CommandStart())
@common_router.message(F.text.lower() == "меню")
async def start_handler(msg: Message, state: FSMContext):
    await state.clear()
    logger.info("Catch start command, handling...")
    await msg.answer(text="Что вы хотите сделать?", reply_markup=menu)


@common_router.message(StateFilter(None), Command(commands=["cancel"]))
@common_router.message(default_state, F.text.lower() == "отмена")
async def cmd_cancel_not(msg: Message, state: FSMContext):
    logger.info("Clearing the data from states")
    await state.set_data({})
    await msg.answer("Отменять нечего.")


@common_router.message(Command(commands=["cancel"]))
@common_router.message(F.text.lower() == "отмена")
@common_router.callback_query(F.data == "cancel_")
async def cmd_cancel(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer(text="Действие отменено")
    await callback.answer()
