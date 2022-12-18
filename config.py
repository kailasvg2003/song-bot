import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", "21967179"))
    API_HASH = os.environ.get("API_HASH", "37d5fbb9217cb56d6261e61305d92748")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5645518503:AAHGXwiZP_SLU8LxwYUoUjYsuYnLQKqw0M0")
    START_MSG = os.environ.get("START_MSG", "<b>Hi {},\nIam A Simple Youtube to Mp3 Downloader Bot,</b>\n\nSend me Any Songs name with /song command")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/2a35fca576aa49de77c98.jpg")
    OWNER = os.environ.get("OWNER", "About_kailas") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
