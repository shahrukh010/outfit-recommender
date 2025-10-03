# logger.py
import logging
import sys

logger = logging.getLogger("outfit recommender")
logger.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] - %(message)s", "%Y-%m-%d %H:%M:%S")

# File handler
file_handler = logging.FileHandler("app.log", mode='w', encoding='utf-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Console handler with UTF-8
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
console_handler.stream.reconfigure(encoding='utf-8')  # fixes Unicode errors on Windows
logger.addHandler(console_handler)
