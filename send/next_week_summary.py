import time
import locale
from icalendar import Calendar

from utils.get_7_day_range_from_today import get_7_day_range_from_today

from services.getData import get_ics_data
from services.sendMessage import send_message_via_WhatsApp
from services.extract_info_from_calendar import get_disposal_dates_from
from services.get_paper_data_as_cal import get_paper_calendar

locale.setlocale(locale.LC_TIME, "de_DE")

def send_next_week_summary():
    startDate, endDate = get_7_day_range_from_today("08.01.2023")
   
    isc_data = get_ics_data()

    try:
        gcal = Calendar.from_ical(isc_data)
        paper_dates = get_paper_calendar()
        
        rest_of_tonnes = get_disposal_dates_from(gcal, startDate, endDate)
        paper_tonne = get_disposal_dates_from(paper_dates, startDate, endDate)

        tonnes = [*rest_of_tonnes, *paper_tonne]
      
        if len(tonnes) == 0:
                    send_message_via_WhatsApp("Nächste Woche muss keine Tonne rausgestellt werden.")          
        else:
            tonnes.sort(key=lambda x: time.mktime(time.strptime(x.get('dtstart').dt.strftime("%Y-%m-%d"),"%Y-%m-%d")))
            is_more_than_one_tonne = len(tonnes) > 1
            string_to_send = f'Nächste Woche {"müssen" if is_more_than_one_tonne else "muss"} {len(tonnes)} {"Tonnen" if is_more_than_one_tonne else "Tonne"} rausgestellt werden:\n'
            for tonne in tonnes:
                string_to_send += f'Am {tonne.get("dtstart").dt.strftime("%A, den %d.%m.")}, die {tonne.get("summary")}.\n'
            send_message_via_WhatsApp(string_to_send.strip())
    except Exception as e:
        error_message = "Irgendwas ging falsch: " + str(e)
        send_message_via_WhatsApp(error_message)