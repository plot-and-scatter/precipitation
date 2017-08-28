Methods
=======

* All stations within 200km of Vancouver that meet [WMO standards](http://climate.weather.gc.ca/climate_normals/normals_documentation_e.html?docID=1981)

* http://climate.weather.gc.ca/advanceSearch/searchHistoricData_e.html

Weather Station Notes
---------------------

ABBOTSFORD A (ID: 702)
* Replaced with 50308 in 2012

ADDENBROKE ISLAND (ID: 374)
* OK

ATLIN (ID: 1485)
* OK

BLUE RIVER A (ID: 1237)
* OK (1237)

BOAT BLUFF (ID: 383)
* OK

CAMPBELL RIVER A (ID: 145)
* OK (145)

CASTLEGAR A (ID: 1105)
* OK (1105)

CHATHAM POINT (ID: 153)
* DQ in 2012, 2013, 2014

COMOX A (ID: 155)
* OK

COWICHAN LAKE FORESTRY (ID: 37)
* DQ in 2014

CRANBROOK A (ID: 1174)
* Replaced with 50818 in 2012

CRESTON (ID: 1111)
* DQ in 2010, 2014

DARFIELD (ID: 1257)
* OK

DAWSON CREEK A (ID: 1404)
* Uses 48208 instead
* Data quality issue in 2013

DRYAD POINT (ID: 387)
* OK

DUNCAN LAKE DAM (ID: 1115)
* OK

ESTEVAN POINT (ID: 244)
* OK

FAUQUIER (ID: 1117)
* DQ in 2011, 2014
* DM in 2010

FORT NELSON A (ID: 1455)
* Replaced with 50819 in 2012

FORT ST JOHN A (ID: 1413)
* Replaced with 50837 in 2012

FRASER LAKE NORTH SHORE (ID: 557)
* DQ in 2010
* DM in 2011-2014

GERMANSEN LANDING (ID: 1415)
* DQ in 2013, 2014

GLACIER NP ROGERS PASS (ID: 1363)
* DQ in 2010-2014

GOLD RIVER TOWNSITE (ID: 246)
* DQ in 2010-2014

GOLDEN A (ID: 1364)
* OK (1364)

GRAND FORKS (ID: 1084)
* DQ in 2010-2014

GREEN ISLAND (ID: 393)
* OK

HIXON (ID: 592)
* DQ in 2010-2014

KAMLOOPS A (ID: 1275)
* Replaced with 51423 in 2013

KLEENA KLEENE 2 (ID: 521)
* DQ in 2010-2014

MARYSVILLE (ID: 1200)
* DQ in 2010-2014

MERRITT STP (ID: 1022)
* OK

MERRY ISLAND LIGHTSTATION (ID: 320)
* DQ in 2010, 2011, 2014

MISSION WEST ABBEY (ID: 810)
* OK

MUD BAY (ID: 187)
* DQ in 2010, 2011, 2012, 2014

NANAIMO A (ID: 192)
* OK (192)

NEW DENVER (ID: 1142)
* Data quality issue in 2010

NOOTKA LIGHTSTATION (ID: 261)
* OK

OSOYOOS WEST (ID: 1043)
* DQ in 2010-2014

PENTICTON A (ID: 1053)
* Replaced with 50269 in 2012

PORT HARDY A (ID: 202)
* Replaced with 51319 in 2012

PRINCE GEORGE A (ID: 631)
* DQ in 2010-2014

PRINCE GEORGE STP (ID: 636)
* OK

PRINCETON A (ID: 1056)
* OK (1056)

QUALICUM R FISH RESEARCH (ID: 208)
* OK

SALTSPRING ST MARY'S L (ID: 93)
* OK

SHAWNIGAN LAKE (ID: 97)
* OK

SMITHERS A (ID: 487)
* OK (487)

SPARWOOD (ID: 1207)
* OK

STEWART A (ID: 434)
* OK (434)

TERRACE A (ID: 441)
* Replaced with 51037 in 2013

TOFINO A (ID: 277)
* OK (277)

TOPLEY LANDING (ID: 496)
* DQ in 2010, 2013, 2014

VANCOUVER INT'L A (ID: 889)
* Replaced with 51442 in 2013

VICTORIA INT'L A (ID: 118)
* Replaced with 51337 in 2013

WHISTLER (ID: 348)
* DQ in 2014

WILLIAMS LAKE A (ID: 664)
* Replaced with 50820 in 2012

* Williams Lake normals are in fact using Victoria normals
* Need to double-check the normals data
  * Williams Lake normals are empty altogether!

Command to generate data
------------------------

ogr2ogr -f GeoJSON -where "sr_sov_a3 in ('can') and iso_3166_2 in ('ca-bc')" provinces.json ne_10m_admin_1_states_provinces_shp.shp

topojson -o output.json --latitude lat --longitude lng --properties -- stations.csv provinces.json
