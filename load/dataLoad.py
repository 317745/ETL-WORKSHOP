import sqlite3
import pandas as pd

def load(table, conn):
    if isinstance(table, list):
        for tName, df in table:
            df.to_sql(tName, conn, if_exists='replace')

    else: 
        df = table[1]
        df.to_sql(table[0], conn, if_exists='replace')