# coding=utf-8

import os
import csv
import requests
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

WMO_NAMES_LIST_FILENAME = "bc_all_stations.txt"
BC_NAMES_LIST_FILENAME = "bc_wmo_stations.txt"

BASE_HISTORICALS_DOWNLOAD_URL = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=%d&Year=%d&Month=5&Day=1&timeframe=2&submit=Download+Data"
BASE_NORMALS_DOWNLOAD_URL = "http://climate.weather.gc.ca/climate_normals//bulkdata_e.html?ffmt=csv&lang=e&prov=BC&yr=1981&stnID=%d&climateID=1100030+++++++++++++&submit=Download+Data"
YEARS = [2010, 2011, 2012, 2013, 2014]

def download_file(url, filename):
  response = requests.get(url)
  with open(filename, "wb") as file:
    file.write(response.content)

def download_historicals(weather_station_name, station_id, year):
  url = BASE_HISTORICALS_DOWNLOAD_URL % (station_id)
  filename = "historicals-%s-id%d-%d.csv" % (weather_station_name.lower().replace(" ", "-"), station_id, year)
  download_file(url, filename)

def download_normals(weather_station_name, station_id):
  url = BASE_NORMALS_DOWNLOAD_URL % (station_id)
  filename = "normals-%s.csv" % (weather_station_name.lower().replace(" ", "-"))
  download_file(url, filename)

def extract_name(line, strip=False):
  name = line[:line.index(" (ID")]
  if strip:
    name = name.replace("'","").replace(".","")
  return name

def extract_id(line):
  station_id = int(line[line.index(":")+2:-2])
  return station_id

weather_station_names = []

with open(WMO_NAMES_LIST_FILENAME, "r") as wmo_file:
  for line in wmo_file:
    name = extract_name(line, True)
    weather_station_names.append(name)
  print weather_station_names

candidates = []

with open(BC_NAMES_LIST_FILENAME, "r") as station_file:
  print "Matching WMO station names"
  for line in station_file:
    name = extract_name(line, True)
    if (name in weather_station_names):
      print bcolors.OKGREEN + "✓ %s" % name + bcolors.ENDC
      candidates.append((name, extract_id(line)))
    else:
      print "✗ %s" % name
  print

for candidate in candidates:
  print "Downloading data for %s" % candidate[0]
  for year in YEARS:
    sys.stdout.write("  %d:   " % year)
    try:
      #download_historicals(candidate[0], candidate[1], year)
      print bcolors.OKGREEN + "  ✓" + bcolors.ENDC
    except Exception:
      print bcolors.FAIL + "  ✗" + bcolors.ENDC
  sys.stdout.write("  Normals:")
  try:
    #download_normals(candidate[0], candidate[1])
    print bcolors.OKGREEN + "  ✓" + bcolors.ENDC
  except Exception:
    print bcolors.FAIL + "  ✗" + bcolors.ENDC
  print
