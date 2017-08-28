# coding=utf-8

from bs4 import BeautifulSoup
import requests
import urlparse

BASE_LIST_URL = "http://climate.weather.gc.ca/advanceSearch/searchHistoricDataStations_e.html?searchType=stnProv&timeframe=1&lstProvince=BC&optLimit=yearRange&StartYear=2010&EndYear=2015&Year=2015&Month=5&Day=10&selRowPerPage=100&cmdProvSubmit=Search&startRow=%d"

MAX_PAGE = 401
PAGE_STEP_SIZE = 100

for page in xrange(1, MAX_PAGE+1, PAGE_STEP_SIZE):
  
  # print page

  url = BASE_LIST_URL % page

  # print url
  
  r = requests.get(url)
  soup = BeautifulSoup(r.text, "html5lib")

  for table in soup.find_all("div", class_="divTable")[0:]:

    for station in table.find_all("form"):
      weather_station = station.find("div", class_="station").text.strip()
      station_id = int(station.find("input", {"name": "StationID"})["value"])
      print "%s (ID: %d)" % (weather_station, station_id)