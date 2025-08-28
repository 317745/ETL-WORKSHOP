from extract.dataExtraction import extraction
from transform.dataTansformation import transformation, GenerateDataSets 
from load.dataLoad import load
from data.querys import kpis
from dashboard.app import app, extractedData

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

    hiresByTechnology = classKpi.hiresByTechnology()
    hiresByYear = classKpi.hiresByYear()
    hiresBySeniority = classKpi.hiresBySeniority()
    hiresByCountryYear = classKpi.hiresByCountryYear()
    hiresByMonthYear = classKpi.hiresByMonthYear(2020)
    applicationsVsHiresByYear = classKpi.applicationsVsHiresByYear()
    
    methods = [
    (hiresByCountryYear, "hiresByCountryYear"),
    (hiresByMonthYear, "hiresByMonthYear"),
    (hiresBySeniority, "hiresBySeniority"),
    (hiresByTechnology, "hiresByTechnology"),
    (hiresByYear, "hiresByYear"),
    (applicationsVsHiresByYear, "applicationsVsHiresByYear")
    ]
    
    data = GenerateDataSets(methods)
    extractedData.extend(data)
    conn.close()

if __name__ == '__main__':
    main()
    app.run(debug=True, port='3333')