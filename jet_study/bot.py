import asyncio
import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sqlalchemy import create_engine

from config import token
from models import Base
from connection import engine

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
)
logger.info("Starting bot...")

storage = MemoryStorage()
bot = Bot(token=token, parse_mode='html')
dp = Dispatcher(bot, storage=storage)

# db init   
Base.metadata.create_all(engine)


if __name__ == '__main__':
    try:
        from handlers import dp
        executor.start_polling(dp, skip_updates=True)
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")