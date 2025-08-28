import pandas as pd

def extraction(path):
    df = pd.read_csv(path).copy()
    df['IdApplication'] = range(1, len(df) + 1)
    df.columns = df.columns.str.replace(' ', '')

    return df

