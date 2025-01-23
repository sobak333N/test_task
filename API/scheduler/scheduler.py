from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

from config import Config
from db.core import sync_engine


jobstores = {
    'default': SQLAlchemyJobStore(url=Config.SYNC_DATABASE_URL, engine=sync_engine)
}

scheduler = AsyncIOScheduler(jobstores=jobstores)
scheduler.start()
