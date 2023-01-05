from utils.is_sunday import is_sunday
from send.next_week_summary import send_next_week_summary
import logging

logging.basicConfig(filename="send.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

if is_sunday(True):
    send_next_week_summary()