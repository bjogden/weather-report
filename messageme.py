from googlevoice import Voice
from googlevoice.util import input
from config import *

def message_me(number, text, **kwargs):
    """ Send me a message using pygooglevoice """
    output = None
    try:
        voice = Voice()
        voice.login(GOOGLE_VOICE_EMAIL, PASSWORD)
        
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                text += " | {}: {}".format(key, value)

        voice.send_sms(number, text)
        output = "Successfully sent text message"

    except Exception, e:
        output = "Error sending message: {}".format(e)
    
    finally:
        return None
        #print output
