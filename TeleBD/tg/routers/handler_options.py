#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.12

from aiogram import Router, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from loguru import logger
from TeleBD.tg.states.state_add import AddOption
from TeleBD.tg.keyboards.kb import cancel
from TeleBD.config import db

router = Router()


@router.message(StateFilter(None), Command("add"))
@router.callback_query(F.data == "add_option")
async def add_option_handler(callback: CallbackQuery, state: FSMContext):
    logger.info("Catch add callback")
    await callback.message.answer(text="Выберите имя услуги", reply_markup=cancel)
    await state.set_state(AddOption.add_name_services)
    await callback.answer(text="")


@router.message(AddOption.add_name_services)
async def add_name_service(msg: Message, state: FSMContext):
    await state.update_data(option_name=msg.text)
    await msg.answer(text="Далее выберите имя картинки(с расширением): ", reply_markup=cancel)
    await state.set_state(AddOption.add_img_name)


@router.message(AddOption.add_img_name)
async def add_img_name(msg: Message, state: FSMContext):
    await state.update_data(img_name=msg.text)
    await msg.answer(text="Далее выберите описание услуги:", reply_markup=cancel)
    await state.set_state(AddOption.add_description_services)


@router.message(AddOption.add_description_services)
async def add_description(msg: Message, state: FSMContext):
    await state.update_data(description=msg.text)
    await msg.answer("Остался последний шаг: цена услуги: ", reply_markup=cancel)
    await state.set_state(AddOption.add_price_services)


@router.message(AddOption.add_price_services)
async def add_price(msg: Message, state: FSMContext):
    logger.info("Updating db...")
    await state.update_data(price=msg.text)
    await msg.answer("Заносим в базу данных.")
    await state.clear()
