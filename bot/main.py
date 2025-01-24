import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.bot import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage, SimpleEventIsolation

from config import Config
from handlers import product_router

print("Initializing bot and dispatcher...")
bot = Bot(
    token=Config.API_KEY, 
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
print("Bot initialized.")

dp = Dispatcher(
    storage=MemoryStorage(), 
    events_isolation=SimpleEventIsolation(),
)
dp.include_routers(product_router)
print("Dispatcher and routers initialized.")


async def main():
    try:
        print("START")
        await bot.delete_webhook(drop_pending_updates=True)
        print("Webhook deleted.")
        await dp.start_polling(
            bot, allowed_updates=dp.resolve_used_update_types()
        )
        print("Polling started.")
    except Exception as e:
        print("Exception occurred:", e)

if __name__ == "__main__":
    asyncio.run(main())
