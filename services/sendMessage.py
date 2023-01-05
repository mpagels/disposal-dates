import os
from dotenv import load_dotenv
load_dotenv()

import logging
import requests

TELEGRAM_KEY = os.getenv("TELEGRAM_KEY")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_message_via_WhatsApp(message):
    logging.info("trying send message")
    url = f"https://api.telegram.org/bot{TELEGRAM_KEY}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}"
    requests.get(url).json()
    logging.info("send message")