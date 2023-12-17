#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.12

from aiogram.fsm.state import StatesGroup, State


class AddOption(StatesGroup):
    """
    State indicate that user use add option
    """
    menu_state = State()
    add_rows = State()


class DeleteOption(StatesGroup):
    """
    State indicate that user use delete option
    """
    delete_state = State()
