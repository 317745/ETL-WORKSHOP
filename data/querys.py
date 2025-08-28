import sqlite3

class kpis:
    def __init__(self, conn):
        self.conn = conn

    def hiresByTechnology(self):
        cursor = self.conn.cursor()
        cursor.execute(f'''
            SELECT COUNT(*) AS Hires, c.Technology AS Technology
            FROM candidates c
            JOIN applications a
                ON a.idApplication = c.idApplication
            WHERE Hired = 1
            GROUP BY c.Technology
        ''')
        data = cursor.fetchall()
        cursor.close()
        return data
    
    def hiresByYear(self):
        cursor = self.conn.cursor()
        cursor.execute(f'''
            SELECT COUNT(*) AS Hires, d.year AS Year
            FROM date d
            JOIN applications a
                ON a.ApplicationDate = d.ApplicationDate
            WHERE a.Hired = 1
            GROUP BY d.year
        ''')
        data = cursor.fetchall()
        cursor.close()
        return data

    def hiresBySeniority(self):
        cursor = self.conn.cursor()
        cursor.execute(f'''
            SELECT COUNT(*) AS Hires, c.Seniority AS Seniority
            FROM candidates c
            JOIN applications a
                ON a.idApplication = c.idApplication
            WHERE a.Hired = 1
            GROUP BY c.Seniority
            ORDER BY Hires ASC
        ''')
        data = cursor.fetchall()
        cursor.close()
        return data
    
    def hiresByCountryYear(self):
        cursor = self.conn.cursor()
        cursor.execute(f''' 
            SELECT COUNT(*) AS Hires, i.Country AS Country, d.year AS Year
            FROM date d
            JOIN applications a
                ON a.ApplicationDate = d.ApplicationDate
            JOIN interview i
                ON a.ApplicationDate = i.ApplicationDate
            WHERE a.Hired = 1
                AND i.Country IN ('United States of America', 'Brazil', 'Colombia', 'Ecuador')
            GROUP BY i.Country 
            ORDER BY d.year
        ''')
        data = cursor.fetchall()
        cursor.close()
        return data
    
    def hiresByMonthYear(self, year = 2025):
        cursor = self.conn.cursor()
        cursor.execute(''' 
            SELECT COUNT(*) AS Hires, d.month AS Month, d.year AS Year
            FROM date d
            JOIN applications a
                ON a.ApplicationDate = d.ApplicationDate
            WHERE a.Hired = 1
                AND d.year = ?
            GROUP BY d.month, d.year
            ORDER BY d.month 
        ''', (year, ))
        data = cursor.fetchall()
        cursor.close()
        return data
    
    def applicationsVsHiresByYear(self):
        cursor = self.conn.cursor()
        cursor.execute(''' 
        SELECT 
            d.year AS Year,
            COUNT(*) AS Applications,
            SUM(CASE WHEN a.Hired = 1 THEN 1 ELSE 0 END) AS Hires
        FROM date d
        JOIN applications a
            ON a.ApplicationDate = d.ApplicationDate
        GROUP BY d.year
        ORDER BY d.year
        ''')
        data = cursor.fetchall()
        cursor.close()
        return data