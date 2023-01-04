import requests 
from utils.file_storage_handler import get_fallback_data, save_file_for_fallback_use


def get_ics_data(dev=False):
    if dev:
        return get_fallback_data("calender.ics")
    else:
        try:
            r = requests.get("https://www.geoport-nwm.de/nwm-download/Abfuhrtermine/ICS/2023/Ortsteil_Wahrsow.ics")
            if r.status_code == 200:
                r.encoding = 'UTF-8'
                save_file_for_fallback_use(r.text, filename="calender.ics")          
                return r.text
            elif r.status_code == 404:
                return get_fallback_data("calender.ics")
        except:
            return get_fallback_data()