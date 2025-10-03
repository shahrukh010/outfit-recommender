from sqlalchemy import text

from app.database.base import Base
from app.database.session import engine
from log.logger import logger
from app.models.user import User

def add_missing_column():
    with engine.connect() as connection:
        connection.execute(text("ALTER TABLE Users ADD COLUMN image varchar(255)"))
        connection.commit()


def init_db():
    logger.info("Initializing database schema...")
    Base.metadata.create_all(bind=engine)
    logger.info("Database schema initialized successfully.")
    # add_missing_column()
