from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

from db.core import sync_engine


def create_scheduler_tables():
    jobstore = SQLAlchemyJobStore(engine=sync_engine)
    jobstore.create_tables()


if __name__ == "__main__":
    create_scheduler_tables()
