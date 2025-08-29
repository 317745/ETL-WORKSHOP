from extract.dataExtraction import extraction
from transform.dataTansformation import transformation, GenerateDataSets 
from load.dataLoad import load
from data.querys import kpis
from dashboard.app import app, graphs

import sqlite3

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
    hiresByMonthYear = classKpi.hiresByMonthYear()
    NotHiresVsHiresByYear = classKpi.NotHiresVsHiresByYear()
    hiresBYCountry = classKpi.hiresBYCountry()
    
    methods = [
        (hiresByCountryYear, "hiresByCountryYear"),
        (hiresByMonthYear, "hiresByMonthYear"),
        (hiresBySeniority, "hiresBySeniority"),
        (hiresByTechnology, "hiresByTechnology"),
        (hiresByYear, "hiresByYear"),
        (NotHiresVsHiresByYear, "NotHiresVsHiresByYear"),
        (hiresBYCountry, "hiresBYCountry")
    ]

    global extractedData 
    extractedData = GenerateDataSets(methods)
    conn.close()

    # Llamar a graphs para actualizar layout
    graphs(extractedData)

if __name__ == '__main__':
    main()
    app.run(debug=True, port=3307)