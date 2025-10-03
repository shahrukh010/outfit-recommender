from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from log.logger import logger
from app.database.settings import database

logger.info("Createing SqlAlchemy engine and session...")
engine = create_engine(database.DB_URL)
logger.info("Engine created successfully.")

# Create session factory
session = sessionmaker(autocommit=False,autoflush=False,bind=engine)
logger.info("Session created successfully.")

def get_db():
    logger.info("Database session created.")
    db = session() # create a new session
    try:
        logger.info("Trying to yield the database session...")
        yield db # yield the session to the caller

    finally:
        db.close()



