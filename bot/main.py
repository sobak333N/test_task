import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.bot import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage, SimpleEventIsolation
from config import Config
from handlers import product_router

try:
    bot = Bot(
        token=Config.API_KEY, 
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
except Exception as e:
    print("Произошла ошибка:", e)

try:
    dp = Dispatcher(
        storage=MemoryStorage(), 
        events_isolation=SimpleEventIsolation(),
    )
    dp.include_routers(product_router)
except Exception as e:
    print("Произошла ошибка:", e)


async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(
            bot, 
            allowed_updates=dp.resolve_used_update_types()
        )
    except Exception as e:
        print("Произошла ошибка:", e)

if __name__ == "__main__":
    asyncio.run(main())