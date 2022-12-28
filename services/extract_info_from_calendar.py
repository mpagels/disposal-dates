from datetime import date

def get_disposal_dates_from(calendar, from_, to):
    tonnes = []
    for component in calendar.walk():
            if component.name == "VEVENT":
                datum = component.get('dtstart').dt.strftime("%Y %m %d").split(" ")
                year, month, day = datum
                currentDate = date(int(year), int(month), int(day))

                if from_ <= currentDate <= to:
                    tonnes.append(component)
    return tonnes