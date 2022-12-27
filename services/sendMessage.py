import os
from dotenv import load_dotenv
load_dotenv()

from twilio.rest import Client

SID=os.getenv('SID')
AUTH=os.getenv('AUTH')
FROM=os.getenv('FROM')
TO=os.getenv('TO')

def send_message_via_WhatsApp(message):
    client = Client(SID, AUTH)
    client.messages.create(body=message,
                       from_=FROM,
                       to=TO)