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



############## old code ################
#from messager import Messager

# weather = pywapi.get_weather_from_weather_com('90048')

# C * 9/5 + 32 = F && (F - 32) * (5/9) = C

# curr_celsius_encoded = weather['current_conditions']['temperature']
# curr_celsius = int(curr_celsius_encoded.encode('utf-8'))
# curr_fah = tempmath.celsius_to_fahr(curr_celsius)

# feels_like_c_encoded = weather["current_conditions"]["feels_like"]
# feels_like_c = int(feels_like_c_encoded.encode("utf-8"))
# feels_like_f = tempmath.celsius_to_fahr(feels_like_c)
# curr_text = weather["current_conditions"]["text"].encode("utf-8")

# location    = weather["location"]["name"].encode("utf-8")
# soonest     = weather['forecasts'][0]
# date        = soonest['date'].encode('utf-8')
# day_text    = soonest['day']['text'].encode('utf-8')
# high_c      = soonest['high'].encode('utf-8')
# high        = tempmath.celsius_to_fahr(int(high_c))
# low_c       = soonest['low'].encode('utf-8')
# low         = tempmath.celsius_to_fahr(int(low_c))
# night_text  = soonest['night']['text'].encode('utf-8')
# sunrise     = soonest['sunrise'].encode('utf-8')
# sunset      = soonest['sunset'].encode('utf-8')
