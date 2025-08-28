import sqlite3
import pandas as pd

def load(table, dbName):
    if isinstance(table, list):
        for tName, df in table:
            conn = sqlite3.connect(dbName)
            df.to_sql(tName, conn, if_exists='replace')
            conn.close

    else: 
        conn = sqlite3.connect(dbName)
        df = table[1]
        df.to_sql(table[0], conn, if_exists='replace')