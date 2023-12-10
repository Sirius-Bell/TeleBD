#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.12

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu = [
    [InlineKeyboardButton(text="📝 Добавить услугу", callback_data="add_option"), InlineKeyboardButton(text="❌ "
                                                                                                           "Удалить "
                                                                                                           "услугу",
                                                                                                      callback_data="delete_option")],
    [InlineKeyboardButton(text="Все услуги", callback_data="all_option")]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)

cancel = [
    [InlineKeyboardButton(text="❌ Отменить действие", callback_data="cancel_")]
]

cancel = InlineKeyboardMarkup(inline_keyboard=cancel)
