# coding=utf-8

import os
import csv

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

HISTORICALS_DIRECTORY_PATH = "historicals"
FIRST_DATA_ROW_INDEX = 27

previous_station = None

for path in os.listdir(HISTORICALS_DIRECTORY_PATH):
  
  if path == ".DS_Store":
    continue
  
  with open(HISTORICALS_DIRECTORY_PATH + os.sep + path) as csv_file:
  
    current_station = path[12:path.index("-id")]
    current_station_id = path[path.index("-id")+3:-9]
  
    if len(current_station_id) < 5:
      while len(current_station_id) < 5:
        current_station_id = "0" + current_station_id
      new_filename = path[:path.index("-id")] + "-id" + current_station_id + path[-9:]
      print "Renaming %s to %s" % (path, new_filename)
      os.rename(HISTORICALS_DIRECTORY_PATH + os.sep + path, HISTORICALS_DIRECTORY_PATH + os.sep + new_filename)

    if previous_station != current_station:
      print ""

    previous_station = current_station
    
    blank_count = 0
    
    reader = csv.reader(csv_file, delimiter=",", quotechar='"')
    for row in reader:
      if reader.line_num >= FIRST_DATA_ROW_INDEX:
        try:
          float(row[19]) # Precipitation column
        except ValueError:
          blank_count += 1
    if blank_count > 364:
      print bcolors.FAIL    + "✗ %s" % path + bcolors.ENDC
    elif blank_count > 50:
      print bcolors.WARNING + "? %s" % path + bcolors.ENDC
    else:
      print bcolors.OKGREEN + "✓ %s" % path + bcolors.ENDC