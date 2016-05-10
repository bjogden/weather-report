import smtplib
from config import *

# AT&T MMS : <number>@mms.att.net
# AT&T Text : <number>@txt.att.net
# Sprint : <number>@messaging.sprintpcs.com
# Verizon : <number>@vtext.com
# T-Mobile : <number>@tmomail.net
# AIM : +1<number>

class Messager(object):
    """ Email as SMS """
    def __init__(self):
        self.email = PYTHON_EMAIL
        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(self.email, PASSWORD)

    def send(self, message, number, carrier):
        c = Messager().get_carrier(carrier)
        self.server.sendmail(self.email, number+c, message)

    def get_carrier(self, carrier):
        try:
            if carrier == "att":
                return "@mms.att.net"
            elif carrier == "atttxt":
                return "@txt.att.net"
            elif carrier == "sprint":
                return "@messaging.sprintpcs.com"
            elif carrier == "verizon":
                return "@vtext.com"
            elif carrier == "tmobile":
                return "@tmomail.com"
            elif carrier == "aim":
                return "+1"
        except Exception, e:
            return None
            txt = "Error getting carrier for '{}': {}".format(carrier, e)
            self.server.sendmail(self.email, MY_NUMBER+"@"+MY_SERVICE, txt)

    def close(self):
        self.server.quit()
