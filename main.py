from extract.dataExtraction import extraction
from transform.dataTansformation import transformation
from load.dataLoad import load
from data.querys import kpis

from datetime import datetime

import sqlite3
import pandas as pd

def main():

    conn = sqlite3.connect('applications.db')

    df = extraction('data/candidates.csv')
    
    transform = transformation(df)

    tables = transform.allTables()

    load(tables, conn)

    classKpi = kpis(conn)

    classKpi.hiresByTechnology()
    classKpi.hiresByYear()
    classKpi.hiresBySeniority()
    classKpi.hiresByCountryYear()
    classKpi.hiresByMonthYear(2020)
    classKpi.applicationsVsHiresByYear()
    conn.close()

if __name__ == '__main__':
    main()