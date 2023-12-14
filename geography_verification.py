import numpy as np
import pandas as pd
from shapely.geometry import Polygon
import matplotlib as plt

from helpers.import_shapefiles import import_shapefiles
from helpers.import_data import import_data 

filepath = "./inputs/fullDownload.geojson"

shapefiles = import_shapefiles(filepath)

print(shapefiles.head())

print(shapefiles['geometry'].info())

print(shapefiles.info())

print(shapefiles['name'].describe())

print(shapefiles['name'].head())