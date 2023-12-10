#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.12

from aiogram.fsm.state import StatesGroup, State


class AddOption(StatesGroup):
    add_name_services = State()
    add_img_name = State()
    add_description_services = State()
    add_price_services = State()
