import requests

def get_fallback_data():
    stream = open('../calender.ics','rb')
    ics = stream.read()
    stream.close()
    return ics

def get_ics_data(dev=False):
    if dev:
        return get_fallback_data()
    else:
        try:
            r = requests.get("https://www.geoport-nwm.de/nwm-download/Abfuhrtermine/ICS/2023/Ortsteil_Wahrsow.ics")
            return r.text
        except:
            return get_fallback_data()