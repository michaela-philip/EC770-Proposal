import numpy as np
import pandas as pd

from helpers.import_data import import_data

def main():
    filepath = 'https://wwwn.cdc.gov/nchs/data/nhanes3/1a/adult.dat'
    colspecs = [(0, 28), (28, 31), (31, 33), (33, -1)]
    columns = ['drop1', 'cofips', 'stfips', 'drop2']
    dropcols = ['drop1', 'drop2']
    adult_data = import_data(filepath, dropcols, columns, colspecs)

    return adult_data 

if __name__ == '__main__':
    main()