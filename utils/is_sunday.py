from datetime import datetime

SUNDAY_AS_NUMBER_6 = 6

def is_sunday(dev=False):
    today_as_number = datetime.today().weekday()
    return SUNDAY_AS_NUMBER_6 == today_as_number if dev == False else True