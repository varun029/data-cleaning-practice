import pandas as pd

def drop_all_rows(df):
    df.dropna()
    print(df)
    print('\n')
    return df

def drop_column(df):
    columns_w_dropped_na=df.dropna(axis=1)
    print('head after dropping columns with atleast one missing value:')
    print(columns_w_dropped_na.head())
    print('\n')
    return columns_w_dropped_na
