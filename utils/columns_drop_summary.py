import pandas as pd

def compare_column_count(df,dropped_na_columns):
    print(f'columns in original dataset: {df.shape[1]}')
    print(f'columns after dropping na values: {dropped_na_columns.shape[1]}')