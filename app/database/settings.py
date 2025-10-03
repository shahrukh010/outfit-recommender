import os

from dotenv import load_dotenv
from log.logger import logger

load_dotenv()
logger.info(".env file loaded")
class DatabaseSettings:
    def __init__(self):
        self.DB_URL =os.getenv("DB_URL")
        self.DB_NAME =os.getenv("DB_NAME")
        self.HOST= os.getenv("DB_HOST")
        self.PORT = os.getenv("DB_PORT")
        self.USER = os.getenv("DB_USER")
        self.PASSWORD = os.getenv("DB_PASSWORD")

        logger.info("DatabaseSettings initialized.")
        logger.info("DB_URL: %s",self.DB_URL)


database = DatabaseSettings()