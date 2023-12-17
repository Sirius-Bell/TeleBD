#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.12

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_opt = [
    [InlineKeyboardButton(text="📝 Добавить значения", callback_data="add_option"),
     InlineKeyboardButton(text="❌ Удалить значения ", callback_data="delete_option")],
    [InlineKeyboardButton(text="Все данные в таблице", callback_data="all_options")]
]

menu_opt = InlineKeyboardMarkup(inline_keyboard=menu_opt)

cancel = [
    [InlineKeyboardButton(text="❌ Отменить действие", callback_data="cancel_")]
]

cancel = InlineKeyboardMarkup(inline_keyboard=cancel)
