import pandas as pd
import numpy as np

#convert into date column to datetime
def convert_to_datetime(df,new_col_name,date_column):
    df[new_col_name]=pd.to_datetime(df[date_column],format='%m/%d/%Y')

    return df[new_col_name]

#checking the length of each entry in the column
#obtain the indices of rows which are in a diff format and print the data

def diff_format_check(df,date_column):
    length_date=df[date_column].str.len()
    print(length_date.value_counts())
    print('\n')

    indices=np.where([length_date!=10])[1]
    print('Indices with corrupted data:', indices)
    print(df.loc[indices])
    print('\n')

def check_column_dtype(df,column_name):
    print(df[column_name].head())
    print('\n')


