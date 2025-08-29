import sqlite3, json

class kpis:
    def __init__(self, conn):
        self.conn = conn

    def _query_to_json(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        columns = [desc[0] for desc in cursor.description]  
        rows = cursor.fetchall()
        cursor.close()
        data = [dict(zip(columns, row)) for row in rows]    
        return data  
                  
    
    def hiresByTechnology(self):
        return self._query_to_json('''
            SELECT 
                COUNT(*) AS Hires, 
                c.Technology AS Technology
            FROM candidates c
            JOIN applications a
                ON a.idApplication = c.idApplication
            WHERE Hired = 1
            GROUP BY c.Technology
        ''')


    def hiresByYear(self):
        return self._query_to_json('''
            SELECT 
                COUNT(*) AS Hires, 
                d.year AS Year
            FROM date d
            JOIN applications a
                ON a.ApplicationDate = d.ApplicationDate
            WHERE a.Hired = 1
            GROUP BY d.year
        ''')
    

    def hiresBySeniority(self):
        return self._query_to_json('''
            SELECT 
                COUNT(*) AS Hires, 
                c.Seniority AS Seniority
            FROM candidates c
            JOIN applications a
                ON a.idApplication = c.idApplication
            WHERE a.Hired = 1
            GROUP BY c.Seniority
            ORDER BY Hires ASC
        ''')
    

    def hiresByCountryYear(self):
        return self._query_to_json(''' 
            SELECT 
                COUNT(*) AS Hires, 
                i.Country AS Country, 
                d.year AS Year
            FROM date d
            JOIN applications a
                ON a.ApplicationDate = d.ApplicationDate
            JOIN interview i
                ON a.ApplicationDate = i.ApplicationDate
            WHERE a.Hired = 1
              AND i.Country IN ('United States of America', 'Brazil', 'Colombia', 'Ecuador')
            GROUP BY i.Country, d.year
            ORDER BY d.year
        ''')
    

    def hiresByMonthYear(self):
        return self._query_to_json(''' 
            SELECT 
                COUNT(*) AS Hires, 
                d.month AS Month, 
                d.year AS Year
            FROM date d
            JOIN applications a
                ON a.ApplicationDate = d.ApplicationDate
            WHERE a.Hired = 1
            GROUP BY d.month, d.year
            ORDER BY d.month 
        ''')
    

    def NotHiresVsHiresByYear(self):
        return self._query_to_json(''' 
            SELECT 
                COUNT(*) as Applications,
                SUM(CASE WHEN Hired = 0 THEN 1 ELSE 0 END) AS TotalNotHires,
                SUM(CASE WHEN Hired = 1 THEN 1 ELSE 0 END) AS TotalHires,
                c.Technology Technology
            FROM candidates c
            JOIN applications a
                ON a.idApplication = c.idApplication
            GROUP BY Technology
        ''')
    

    def hiresBYCountry(self):
        return self._query_to_json('''
            SELECT 
                COUNT(*) Hires, 
                i.Country Country
            FROM interview i 
            JOIN applications a
                ON a.idApplication = i.idApplication
            WHERE Hired = 1
            GROUP BY Country
            ORDER BY Hires ASC;
        ''')
