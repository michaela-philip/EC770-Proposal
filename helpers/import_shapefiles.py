import pandas as pd
import geopandas as gpd

def import_shapefiles(filepath):
    data = gpd.read_file(filepath)
    return data

