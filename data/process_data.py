import os
import csv
import copy

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

HISTORICALS_DIRECTORY_PATH = "historicals_stitched"
NORMALS_DIRECTORY_PATH = "normals"

HISTORICALS_FIRST_DATA_LINE = 6
NORMALS_PRECIP_DATA_LINE = 28

OUTPUT_FILE = "draft-data.csv"

MAX_ERRORS_PER_MONTH = 10

YEARS = [2010, 2011, 2012, 2013, 2014]
MONTHS_PER_YEAR = 12

def format_month(errors, color):
  return "%s%s%s" % (color, "{0:3}".format(errors), bcolors.ENDC)

def print_error_format(station_name, error_data):
  print
  print "%s" % station_name
  print
  print "Year    J  F  M  A  M  J  J  A  S  O  N  D"
  print "------------------------------------------"
  for year in YEARS:
    formatted_monthly_errors = ""
    for month in range(0, MONTHS_PER_YEAR):
      errors = error_data[year][month]
      if errors > MAX_ERRORS_PER_MONTH:
        formatted_monthly_errors += format_month(errors, bcolors.FAIL)
      elif errors > 0:
        formatted_monthly_errors += format_month(errors, bcolors.WARNING)
      else:
        formatted_monthly_errors += format_month(errors, bcolors.ENDC)

    print "%d: %s" % (year, formatted_monthly_errors)


with open(OUTPUT_FILE, "w") as output_file:
  writer = csv.writer(output_file, delimiter=",", quotechar='"')
  header_items = ["station_name","lat","lng","elevation"]
  for year in YEARS:
    for month in range(1, MONTHS_PER_YEAR+1):
      header_items.append("%d-%s" % (year, "{:02d}".format(month)))
  writer.writerow(header_items)

for path in os.listdir(HISTORICALS_DIRECTORY_PATH):
  if path == ".DS_Store":
    continue

  with open(HISTORICALS_DIRECTORY_PATH + os.sep + path) as csv_file:
    reader = csv.reader(csv_file, delimiter=",", quotechar='"')

    station_name = reader.next()[1]
    province = reader.next()[1]
    lat = reader.next()[1]
    lng = reader.next()[1]
    elevation = reader.next()[1]
    
    # Set up precip and error data dicts
    precip_data = {}
    error_data = {}

    for year in YEARS:
      precip_data[year] = []
      error_data[year] = []
      for month in range(1, MONTHS_PER_YEAR+1):
        precip_data[year].append(0)
        error_data[year].append(0)

    for row in reader:
      if reader.line_num > HISTORICALS_FIRST_DATA_LINE:
        year = int(row[1])
        month = int(row[2])
        try:
          precip = float(row[19])
          precip_data[year][month-1] += precip
        except ValueError:
          error_data[year][month-1] += 1

    bad_station = False

    for year in error_data:  
      for month in range(0, MONTHS_PER_YEAR):
        month_errors = 0
        month_errors += error_data[year][month]
        if month_errors > MAX_ERRORS_PER_MONTH:
          bad_station = True
    
    if bad_station:
      print_error_format(station_name, error_data)
    
    else:
      # Now get normals data
      normals_path = NORMALS_DIRECTORY_PATH + os.sep + "normals-%s.csv" % station_name.lower().replace(" ", "-").replace("'","").replace(".","")
      #print normals_path
      with open(normals_path, "r") as normals_file:
        #print normals_file
        normals_reader = csv.reader(normals_file, delimiter=",", quotechar='"')
        for row in normals_reader:
          if normals_reader.line_num == NORMALS_PRECIP_DATA_LINE:
            normal_precip_data = row[1:-2] # Gets Jan - Dec data

      with open(OUTPUT_FILE, "a") as output_file:
        writer = csv.writer(output_file, delimiter=",", quotechar='"')
        row = [station_name, lat, lng, elevation]

        for year in YEARS:
          for month in range(0, MONTHS_PER_YEAR):
            row.append("{0:.2f}".format(precip_data[year][month]))

        writer.writerow(row)

        row = [station_name + " NORMALS", lat, lng, elevation]

        for year in YEARS:
          for month in range(0, MONTHS_PER_YEAR):
            row.append("{0:.2f}".format(float(normal_precip_data[month])))

        writer.writerow(row)
