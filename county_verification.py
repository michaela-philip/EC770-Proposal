import numpy as np
import pandas as pd

from helpers.import_crosswalk import import_crosswalk
from helpers.import_data import import_data
from helpers.import_shapefiles import import_shapefiles


filepath_0 = 'https://www2.census.gov/geo/docs/reference/codes2020/place_by_cou/st'
crosswalk = import_crosswalk(filepath_0)

filepath = 'https://wwwn.cdc.gov/nchs/data/nhanes3/1a/adult.dat'
colspecs = [(0, 28), (28, 31), (31, 33), (33, -1)]
columns = ['drop1', 'cofips', 'stfips', 'drop2']
dropcols = ['drop1', 'drop2']
adult_data = import_data(filepath, dropcols, columns, colspecs)

filepath = "./inputs/fullDownload.geojson"
shapefiles = import_shapefiles(filepath)

print(adult_data.head())
print(crosswalk.head())
print(shapefiles.head())

crosswalk.rename({'STATEFP':'stfips', 'COUNTYFP':'cofips', 'PLACENAME':'city'}, axis = 1, inplace = True)

shapefile_to_county = shapefiles.merge(crosswalk, how = 'left', on  = 'city')
print(shapefile_to_county.head())

geo_match = adult_data.merge(shapefile_to_county, how = 'left', on = ['stfips', 'cofips'])
print(geo_match.head())


# print(adult_data.shape)

# 
# geo_match = adult_data.merge(crosswalk, how = 'inner', on = ['stfips', 'cofips'])

# print(geo_match.describe())