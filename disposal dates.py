from utils.is_sunday import is_sunday
from send.next_week_summary import send_next_week_summary

if is_sunday(True):
    send_next_week_summary()