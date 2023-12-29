import numpy as np
import pandas as pd

from helpers.import_data import import_data

def main():
    filepath = 'https://wwwn.cdc.gov/nchs/data/nhanes3/1a/adult.dat'
    colspecs = [(0, 28), (28, 31), (31, 33), (33, -1)]
    columns = ['drop1', 'cofips', 'stfips', 'drop2']
    dropcols = ['drop1', 'drop2']
    adult_data = import_data(filepath, dropcols, columns, colspecs)

    adult_data.to_csv('./adult_data.csv')

    print("adult csv created")

    filepath = 'https://wwwn.cdc.gov/nchs/data/nhanes3/1a/youth.dat'
    youth_data = import_data(filepath, dropcols, columns, colspecs)

    youth_data.to_csv('./youth_data.csv')

    print("youth csv created")


if __name__ == '__main__':
    main()