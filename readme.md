This script sends a message with disposal dates calculated for the next week from an isc file, every sunday.

## ToDos

Schicke Sonntag abends eine Nachricht mit einer Übersicht, der Tonnen, die die nächste Woche rausgestellt werden müssen

Schicke Erinnerung, das morgen eine bestimmte Tonne ist

Schicke Erinnerung, das heute eine bestimmte Tonne ist

Zusammenfassung

- download ics from https://www.geoport-nwm.de/de/abfuhrtermine-geoportal.html to be always up to date
- Calculate next week

  - when script starts, check if sunday, if, then calculate
    create time range from today to next sunday
  - then get ics
  - then extract next tonnes for this week
  - send text via telegram

- check if a tonne is in between
- send dates of tonnes or info that no tonne is planned
