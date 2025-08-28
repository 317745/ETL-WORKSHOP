from extract.dataExtraction import extraction
from transform.dataTansformation import transformation
from load.dataLoad import load

from datetime import datetime

import pandas as pd

def main():

    df = extraction('data/candidates.csv')
    
    transform = transformation(df)

    tables = transform.allTables()

    load(tables, 'applications.db')

if __name__ == '__main__':
    main()