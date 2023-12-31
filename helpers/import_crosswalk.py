import numpy as np
import pandas as pd

def import_crosswalk(filepath_0, limit = None):
    output = pd.DataFrame()
    lst = []
    counter = 0
    stfips_abbrev = {'01':'al', '02':'ak', '04':'az', '05':'ar', '06':'ca', '08':'co', '09':'ct', '10':'de', '11':'dc', '12':'fl', '13':'ga', '15':'hi', '16':'id', '17':'il', '18':'in', '19':'ia', '20':'ks', '21':'ky', '22':'la', '23':'me', '24':'md', '25':'ma', '26':'mi', '27':'mn', '28':'ms', '29':'mo', '30':'mt', '31':'ne', '32':'nv', '33':'nh', '34':'nj', '35':'nm', '36':'ny', '37':'nc', '38':'nd', '39':'oh', '40':'ok', '41':'or', '42':'pa', '44':'ri', '45':'sc', '46':'sd', '47':'tn', '48':'tx', '49':'ut', '50':'vt', '51':'va', '53':'wa', '54':'wv', '55':'wi', '56':'wy', '72':'pr'}
    for key in stfips_abbrev:
        filepath = filepath_0 + str(key) + '_' + str(stfips_abbrev[key]) + '_place_by_county2020.txt'
        intermed = pd.read_csv(filepath, sep = '|', dtype = str)
        output = pd.concat([output, intermed])
        counter += 1
        if counter == limit:
            break

    return output
print('crosswalk completed')

if __name__ == '__main__':
    raise RuntimeError('This script is not intended to be run directly.')