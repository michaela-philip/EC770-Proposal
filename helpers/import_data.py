import numpy as np
import pandas as pd

def import_data(filepath, dropcols, columns, colspecs, limit=None):
    output = pd.read_fwf(filepath, colspecs = colspecs, header=None, nrows=limit, dtype = str)
    output.columns = columns
    output = output.drop(columns = dropcols)

    return output
print('import completed')

if __name__ == '__main__':
    raise RuntimeError('This script is not intended to be run directly.')
