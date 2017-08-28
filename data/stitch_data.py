# coding=utf-8

import os
import csv
from itertools import islice

HISTORICALS_DIRECTORY_PATH = "historicals_raw"
FIRST_DATA_ROW_INDEX_IN_INPUT_FILE = 27
FIRST_DATA_ROW_INDEX_IN_OUTPUT_FILE = 7

previous_station_name = None
previous_year = None

output_path = None

for path in os.listdir(HISTORICALS_DIRECTORY_PATH):
  
  if path == ".DS_Store":
    continue
  
  # Loop through all the historical data files
  with open(HISTORICALS_DIRECTORY_PATH + os.sep + path) as csv_file:
    
    current_station_name = path[12:path.index("-id")]
    current_year = int(path[-8:-4])

    reader = csv.reader(csv_file, delimiter=",", quotechar='"')

    if current_station_name != previous_station_name:
      
      output_path = "historicals_stitched" + os.sep + "historicals-%s.csv" % current_station_name
      print output_path

      with open(output_path, "w") as output:
        writer = csv.writer(output, delimiter=",", quotechar='"')
        writer.writerow(["station_name", reader.next()[1]])
        writer.writerow(["province", reader.next()[1]])
        writer.writerow(["latitude", reader.next()[1]])
        writer.writerow(["longitude", reader.next()[1]])
        writer.writerow(["elevation", reader.next()[1]])
        while (reader.line_num < FIRST_DATA_ROW_INDEX_IN_INPUT_FILE - 2): # This will get us the header row
          reader.next()
        writer.writerow(reader.next())

    # CASE 1 of 2: The weather stations were switched; special stitch
    if previous_year == current_year:
      
      # Use a temporary file to hold interim results
      temp_path = output_path + ".tmp.csv"

      # First, determine how many "valid" lines there are in the output.
      # (When the weather station is retired, there will be a long run of
      # lines with no data; we want to snip them.)
      with open(output_path, "r") as source_file:
        source_reader = csv.reader(source_file, delimiter=",", quotechar='"')
        last_line_index = 0
        for row in source_reader:
          if source_reader.line_num >= FIRST_DATA_ROW_INDEX_IN_OUTPUT_FILE:
            try:
              float(row[19])
              last_line_index = source_reader.line_num
            except ValueError:
              pass
        # Now last_line_index == the last valid line in the file
        
        source_file.seek(0) # Reset the reader
        source_reader = csv.reader(source_file, delimiter=",", quotechar='"')
        
        with open(temp_path, "w") as temp_file:
          temp_writer = csv.writer(temp_file, delimiter=",", quotechar='"')

          # Now we will copy those valid lines to a new temp file
          for row in source_reader:
            if source_reader.line_num <= last_line_index:
              temp_writer.writerow(row)

          # Next, we will also copy the valid lines from the *new* (current)
          # weather station data file to the temp file, ignoring the first
          # lines that are invalid (again, blank). Note we can't do this in
          # the same way as when the weather stations were not switched: in
          # that case, we want to preserve empty lines because they indicate
          # data quality issues.
          for row in reader:
            if reader.line_num > FIRST_DATA_ROW_INDEX_IN_INPUT_FILE:
              try:
                float(row[19])
                temp_writer.writerow(row)
              except ValueError:
                pass

      # Remove the original file, and rename the temp file
      os.remove(output_path)
      os.rename(temp_path, output_path)
    
    # CASE 2 of 2: The weather stations were not switched
    else:
      with open(output_path, "a") as output:
        writer = csv.writer(output, delimiter=",", quotechar='"')
        for row in reader:
          if reader.line_num >= FIRST_DATA_ROW_INDEX_IN_INPUT_FILE:
            writer.writerow(row)

    # Finishing up this iteration of the loop: set prev to current
    previous_station_name = current_station_name
    previous_year = current_year