from datetime import datetime
import pandas as pd


class transformation:
    def __init__(self, df):
        self.df = df

    def factTableApplication(self):
        self.df['ApplicationDate'] = pd.to_datetime(self.df['ApplicationDate'], format ='%Y-%m-%d')
        self.df['Hired'] = [1 if codeS>= 7 and techS >= 7 else 0 
                            for codeS, techS in zip(self.df['CodeChallengeScore'], self.df['TechnicalInterviewScore'])]

        return ('applications', self.df[['IdApplication', 'ApplicationDate', 'CodeChallengeScore','TechnicalInterviewScore', 'Hired']])

    def tableDate(self):
        self.df['ApplicationDate'] = pd.to_datetime(self.df['ApplicationDate'], format ='%Y-%m-%d')

        self.df['year'] = self.df['ApplicationDate'].dt.year
        self.df['month'] = self.df['ApplicationDate'].dt.month
        self.df['day'] = self.df['ApplicationDate'].dt.day
        
        return ('date', self.df[['ApplicationDate', 'year', 'month', 'day']])
    
    def tableCandidate(self):
        return ('candidates', self.df[['IdApplication', 'FirstName', 'LastName', 'Email', 'YOE', 'Seniority', 'Technology']])
    
    def tableINterview(self):
        self.df['ApplicationDate'] = pd.to_datetime(self.df['ApplicationDate'], format ='%Y-%m-%d')

        return ('interview', self.df[['IdApplication', 'ApplicationDate', 'Country']])
    
    def allTables(self):
        return [self.factTableApplication(), self.tableDate(), self.tableCandidate(), self.tableINterview()]