#!/usr/bin/env python
__author__ = "Jonathan Mann"
__email__ = "jonathan.william.mann@gmail.com"

import urllib2
from bs4 import BeautifulSoup

class WeatherMiner:
    """
    API to collect weather data from Weather Underground

    Attributes:
        api_string (string): url to plug inputs into to pull weather data
        weather_keys (list): keys to match with retrieved weather data
    """
    def __init__(self):
        self.api_string = "https://www.wunderground.com/history/airport/{AIRPORT}/{YEAR}/{MONTH}/{DAY}/DailyHistory.html"
        self.weather_keys = ['mean','high','avg-high','record-high','low','avg-low','record-low']
    def get_weather(self,year,month,day,airport="KJRB"):
        """
        API call to retrieve weather

        Args:
            year (int): year to pull
            month (int): month to pull
            day (int): day to pull
            airport (string): airport to retrieve weather data for
        Returns:
            weather_data (dict): temperatures for requested day
        """
        req_url = self.api_string.format(AIRPORT=airport,YEAR=year,MONTH=month,DAY=day)
        raw_data = BeautifulSoup(urllib2.urlopen(req_url).read(),"lxml").find("table",{"id":"historyTable"}).findAll("span",{"class":"wx-value"})
        weather_floats = [float(x.text) for x in raw_data]
        weather_data = dict(zip(self.weather_keys,weather_floats))
        return weather_data

if __name__ == '__main__':
    w = WeatherMiner()
    print(w.get_weather(2018,2,4))

#['mean','high','avg-high','record-high','low','avg-low','record-low','dew-point','precipitation','wind-speed','max-wind','gusts','visibility']

