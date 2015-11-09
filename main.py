#!/usr/bin/env python
__author__ = "Bryce Ogden"

import pywapi 
import pprint, time, datetime
import logging, os
import tempmath
from config import *
from tmessage import MessageMe

pp = pprint.PrettyPrinter(indent=4)

log_file = log_path+'weather.log'
logging.basicConfig(level=logging.INFO,
                    format="%(message)s",
                    filename=log_file,
                    filemode='a+')

now  = datetime.datetime.now()
year = now.strftime("%Y")

count = 0

m = MessageMe()

for z in recipients:
    count      += 1
    zipcode     = z

    weather     = pywapi.get_weather_from_weather_com(zipcode)

    location    = weather["location"]["name"].encode("utf-8")
    soonest     = weather['forecasts'][0]

    date        = soonest['date'].encode('utf-8')
    day_text    = soonest['day']['text'].encode('utf-8')
    high_c      = soonest['high'].encode('utf-8')
    high        = tempmath.celsius_to_fahr(int(high_c))
    low_c       = soonest['low'].encode('utf-8')
    low         = tempmath.celsius_to_fahr(int(low_c))
    night_text  = soonest['night']['text'].encode('utf-8')
    sunrise     = soonest['sunrise'].encode('utf-8')
    sunset      = soonest['sunset'].encode('utf-8')

    # iterate recipients per zipcode
    for i in recipients[z]:
        if i['notify']:
            text_message = ("""Good morning, %s!
        %s - high: %s""" % (i['name'], date, high))
            if len(day_text) > 0:
                text_message += (" %s @ day" % day_text.lower())
            text_message += (" | low: %s" % low)
            if len(night_text) > 0:
                text_message += (" %s @ night" % night_text.lower())
            text_message += (" in %s." % location)
            text_message += (" \nSunrise: %s | Sunset: %s" % (sunrise, sunset))
            text_message += (" \nHave a great day!")

            # old google voice sms
            #message_me(i['number'], text_message)
            m.send_sms(i['number'], text_message)

    #print date, high, low, zipcode, sunrise, sunset, day_text, night_text
    # Date,High,Low,Zipcode,Sunrise,Sunset,DayText,NightText
    log_text = "%s,%s,%s,%s,%s,%s,%s,%s,%s" % (date, high, low, zipcode, sunrise, sunset, day_text, night_text, year)
    print log_text
    logging.info(log_text)

    time.sleep(5) # so pywapi/google voice APIs aren't pinged too quickly

