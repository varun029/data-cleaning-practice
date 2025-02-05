import pandas as pd

def fill_zero(df):
    df.fillna(0)
    print(df)
    print('\n')
    return df

def fill_mean(df):
    df.fillna(df.mean())
    print(df)
    print('\n')
    return df

def fill_median(df):
    df.fillna(df.median())
    print(df)
    print('\n')
    return df

def fill_next_val(df):
    df.fillna(method='bfill',axis=1).fillna(0)
    print(df)
    print('\n')
    return df


