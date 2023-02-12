# Importing modules
from twilio.rest import Client
import os

TWILIO_SID = os.environ.get("T_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("T_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.environ.get("T_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.environ.get("MY_NUMBER")


class NotificationManager:
    """Sends sms messages"""

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        """Sends a sms message"""
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent
        print(message.sid)
