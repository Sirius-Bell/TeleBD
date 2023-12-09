from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from loguru import logger

router = Router()


@router.message(CommandStart())
async def start_handler(msg: Message):
    logger.info("Catch start command, handling...")
    await msg.answer("Simple checks...")
