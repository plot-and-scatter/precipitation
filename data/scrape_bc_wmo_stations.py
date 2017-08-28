# coding=utf-8

from bs4 import BeautifulSoup
import requests
import urlparse

BASE_LIST_URL = "http://climate.weather.gc.ca/climate_normals/stnselect_1981_2010_e.html?lang=e&province=BC&provSubmit=go&page=%d"
YEARS = [2010, 2011, 2012, 2013, 2014]

MAX_PAGE = 251
PAGE_STEP_SIZE = 25

for page in xrange(1, MAX_PAGE+1, PAGE_STEP_SIZE):

  url = BASE_LIST_URL % page
  
  r = requests.get(url)
  soup = BeautifulSoup(r.text, "html5lib")

  for table in soup.find_all("table", class_="wet-boew-zebra")[0:]:
    for row in table.find_all("tr")[1:]:
      weather_station = row.find("td")
      if weather_station.text.startswith("*"):
        link = weather_station.find("a")
        parsed_link = urlparse.urlparse(link["href"])
        station_id = int(urlparse.parse_qs(parsed_link.query)["stnID"][0])
        weather_station_name = weather_station.text[2:]
        weather_station_pretty_name = weather_station_name.lower().replace(" ", "-")
        print "%s (ID: %d)" % (weather_station_name, station_id)
