import forecastio 
import arrow #A much mooooooore friendlier version than datetime package. I found my new datetime love!
import json 
import datetime as dt
from progressbar import ProgressBar
import time 
import re 
import pandas as pd 
from itertools import chain
import itertools
import pytz



pbar=ProgressBar()

"""
Forecastio is a great website for grabbing weather data. For the free version, they're only allowing 1000 API calls per day. 
But for every call, you'll grab 1 day of comprehensive data. Check out their website!
https://developer.forecast.io/
"""




api_key = 'd2af52fa407f31e459ca628c71c9edae'
lati = '37.817773'
long = '-122.272232'

start = dt.datetime(2006,1,1)
end = dt.datetime(2008,1,1)

with open('weather_2006-01-01---2008-01-01.json', 'a+') as file:
    for c_date in pbar(arrow.Arrow.range('day', start, end)):
        fore = forecastio.load_forecast(api_key, lati, long,time=c_date)
        data=fore.json
        json.dump(data, file)
        file.write('\n')
        print c_date

'''header_chk=0
file = open('weather_2008-01-01---2010-01-01.json', 'rb').readlines()
for i in file:
    df = pd.read_json(i,orient='series')
    #print df['daily']['data'][0].keys()
    try:
        hourly = pd.DataFrame(df['daily']['data'][0],index=(pd.to_datetime(df['daily']['data'][0]['time'],unit='s').date(),),
                                                columns=[u'summary', u'sunriseTime', u'apparentTemperatureMinTime', u'moonPhase', u'icon', u'precipType', u'apparentTemperatureMax', u'temperatureMax', u'time', u'apparentTemperatureMaxTime', u'sunsetTime', u'pressure', u'windSpeed', u'temperatureMin', u'apparentTemperatureMin', u'windBearing', u'temperatureMaxTime', u'temperatureMinTime'])
        with open('weather_2008-01-01---2010-01-01.csv','ab') as f:
    
            if header_chk >= 1:
                hourly.to_csv(f,header=False)
            else:
                header_chk+=1
                hourly.to_csv(f)
    except KeyError:
        print "End of the line"
'''



