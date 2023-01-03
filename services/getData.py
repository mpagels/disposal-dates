import requests 

def get_fallback_data():
    stream = open('calender.ics','rb')
    ics = stream.read()
    stream.close()
    return ics

def save_file_for_fallback_use(text, filename):
    with open(filename, "w") as ics:
        ics.write(text)

def get_ics_data(dev=False):
    if dev:
        return get_fallback_data()
    else:
        try:
            r = requests.get("https://www.geoport-nwm.de/nwm-download/Abfuhrtermine/ICS/2023/Ortsteil_Wahrsow.ics")
            if r.status_code == 200:
                r.encoding = 'UTF-8'
                save_file_for_fallback_use(r.text, filename="calender.ics")
                return r.text
            elif r.status_code == 404:
                return get_fallback_data()
        except:
            return get_fallback_data()