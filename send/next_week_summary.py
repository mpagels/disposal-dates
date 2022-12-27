import time
import locale
from datetime import date

from utils.get_7_day_range_from_today import get_7_day_range_from_today

from services.getData import get_ics_data
from services.sendMessage import send_message_via_WhatsApp

from icalendar import Calendar

locale.setlocale(locale.LC_TIME, "de_DE")

def send_next_week_summary():
    startDate, endDate = get_7_day_range_from_today()

    tonnes = []
   
    isc_data = get_ics_data()

    try:
        gcal = Calendar.from_ical(isc_data)
    
        for component in gcal.walk():
            if component.name == "VEVENT":
                datum = component.get('dtstart').dt.strftime("%Y %m %d").split(" ")
                year, month, day = datum
                currentDate = date(int(year), int(month), int(day))

                if startDate <= currentDate <= endDate:
                    tonnes.append(component)

        if len(tonnes) == 0:
                    send_message_via_WhatsApp("Nächste Woche muss keine Tonne rausgestellt werden.")          
        else:
            tonnes.sort(key=lambda x: time.mktime(time.strptime(x.get('dtstart').dt.strftime("%Y-%m-%d"),"%Y-%m-%d")))
            is_more_than_one_tonne = len(tonnes) > 1
            print(f'Nächste Woche {"müssen" if is_more_than_one_tonne else "muss"} {len(tonnes)} {"Tonnen" if is_more_than_one_tonne else "Tonne"} rausgestellt werden:')
            for tonne in tonnes:
                print(f'Am {tonne.get("dtstart").dt.strftime("%A, den %d.%m.")}, die {tonne.get("summary")}.')
    except Exception as e:
        error_message = "Irgendwas ging falsch: " + str(e)
        send_message_via_WhatsApp(error_message)