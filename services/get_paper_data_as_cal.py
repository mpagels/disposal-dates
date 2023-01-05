from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

import logging

from utils.file_storage_handler import save_file_for_fallback_use, get_fallback_data

from bs4 import BeautifulSoup

from icalendar import Calendar, Event
from datetime import datetime

# dev-start
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
# dev-end

def get_paper_calendar():
    
    try:
        logging.info("start scraping paper dates") 
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.ger-umweltschutz.de/abfuhrplaene.html")
        time.sleep(2)
        # assert "Python" in driver.title
        # next two lines are not needed in 2023 right now (04.01.2023)
        # might be usefule when the 2024 dates are here
        #select = Select(driver.find_element(By.CLASS_NAME, "form-control")) 
        #select.select_by_index(1)
        #time.sleep(0.5)
        input_ = driver.find_element(By.ID, "ort")
        input_.send_keys("Wahrsow")
        time.sleep(0.5)
        input_.send_keys(Keys.DOWN, Keys.RETURN)
        time.sleep(0.5)
        tbody = driver.find_element(By.TAG_NAME, "tbody")
        soup = BeautifulSoup(tbody.get_attribute('innerHTML'), 'html.parser')
        driver.close()

        paper_dates = []

        class_ap = soup.find_all("td", class_="ap")

        # init the calendar
        cal = Calendar()

        # Some properties are required to be compliant
        cal.add('prodid', '-//My calendar product//example.com//')
        cal.add('version', '2.0')

        for element in class_ap:
            # Add subcomponents
            day, month, _ = element.find("span").get_text().split(",")[1].strip().split(".")

            event = Event()
            event.add('name', 'VEVENT Meeting')
            event.add('summary', 'Papiertonne')
            event.add('dtstart', datetime(2023, int(month), int(day), 5, 0, 0))
            event.add('dtend', datetime(2023, int(month), int(day),20, 0, 0))    
            cal.add_component(event)

        save_file_for_fallback_use(cal.to_ical().decode("utf-8").replace('\r\n', '\n').strip(), "paper_calender.ics")
        logging.info("done scrapping") 
        return cal
    except:
        logging.info("error scrapping") 
        cal = get_fallback_data("paper_calender.ics") 
        return Calendar.from_ical(cal)
        

