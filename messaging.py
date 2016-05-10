__author__ = "Bryce Ogden"

from twilio.rest import TwilioRestClient
from config import *

class Message(object):

    def __init__(self):
        # To find these visit https://www.twilio.com/user/account
        ACCOUNT_SID = TWILIO_ACCT_SID
        AUTH_TOKEN = TWILIO_AUTH_TOKEN
        self.client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, num, text):
        """ Sends SMS to number, with optional text(?) 
            Rates: $0.0075 to send
                   $0.0075 to receive
        """
        message = self.client.messages.create(
            body = text, # optional
            to = num,
            from_ = TWILIO_NUMBER
        )
        #print message.sid

    def send_mms(self, num, text, image_url):
        """ Sends MMS to number, text optional.
            image_url: can be string (ex. "http://example.com/cat.jpg") OR
               can be list of strings (ex. [".../cat.jpg", ".../dog.jpg"])
            Rates: $0.02 to send
                   $0.01 to receive
        """
        message = self.client.messages.create(
            body = text, # optional
            to = num,
            from_ = TWILIO_NUMBER,
            media_url = image_url
        )
