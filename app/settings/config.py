import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.TELEGRAM_BOT_KEY = os.getenv("TELEGRAM_BOT_KEY")
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
        self.URL_BASE = os.getenv("URL_BASE", "https://www.bcv.org.ve")
        self.APP_NAME = os.getenv("APP_NAME", "HoróscopoBot")
        self.AUTHOR_NAME = os.getenv("AUTHOR_NAME", "Anjiver")