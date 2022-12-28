from datetime import datetime, timedelta, date

def get_7_day_range_from_today(dev_today = False):
    today_as_date = datetime.today() if dev_today == False else datetime.strptime(dev_today, "%d.%m.%Y")
    seven_days_From_today_as_date =  today_as_date + timedelta(days=7)
    return [today_as_date.date(), seven_days_From_today_as_date.date()]


