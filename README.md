# weather-report
Using Google's Python weather API to retrieve weather by zip code and log data, Twilio to message the weather info, and Google's JS Visualization API to parse JSON log from Python to render client-side visualizations. Visit [this great page](http://bryceogden.com/weather/ "bryceogden.com/weather") to see the charts that are dynamically updated daily and learn more!

List of tools used:
- Python: to gather weather data, message weather info to people, upload formatted data to S3
  - [Twilio](https://www.twilio.com/ "https://www.twilio.com/")~~/SMTP/Google Voice API~~: service to send messages
  - [Google Weather API w/ Weather.com data](https://pypi.python.org/pypi/pywapi "https://pypi.python.org/pypi/pywapi"): service used to get weather data (pywapi now deprecated)
- [Raspberry Pi](https://www.raspberrypi.org/products/raspberry-pi-2-model-b/ "https://www.raspberrypi.org/products/raspberry-pi-2-model-b/"): Python-portion of project is being run on one of these in my living room
- JavaScript/jQuery: to create attractive web page
  - [Google Visualization API](https://developers.google.com/chart/interactive/docs/reference "https://developers.google.com/chart/interactive/docs/reference"): develop aesthetically pleasing charts
  - AJAX: to get data from S3 to web page
  - JSON: how data is stored on S3
- AWS S3: storage of weather data

I formerly used [SMTP](https://docs.python.org/2/library/smtplib.html "https://docs.python.org/2/library/smtplib.html") and the [Google Voice API](https://pypi.python.org/pypi/pygooglevoice/0.5 "https://pypi.python.org/pypi/pygooglevoice/0.5") to deliver the daily, morning weather messages, but these were unreliable -- the messages would either be missing text or not be delivered at all. Not to mention, the SMS Google Voice API is now deprecated.
