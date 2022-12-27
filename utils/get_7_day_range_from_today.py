from datetime import datetime, timedelta, date

def get_7_day_range_from_today():
    today_as_date = datetime.today()
    seven_days_From_today_as_date =  today_as_date + timedelta(days=7)
    return [today_as_date.date(), seven_days_From_today_as_date.date()]


