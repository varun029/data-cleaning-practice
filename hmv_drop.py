'''
Steps to handle missing values
1. Take a first look at the data
2. How many missing data points do we have?
3. Figure out why data is missing
4. Drop missing values / Filling in missing values
'''

import pandas as pd
import numpy as np

#reading the csv file
permit_data=pd.read_csv('/Users/vandana/Desktop/data-cleaning-practice/Building_Permits.csv')
print(permit_data.head())
print('\n')

#set seed for reproductibility
np.random.seed(0)

#finding missing values per column
missing_values=permit_data.isnull().sum()
print('The number of missing values per column are: ')
print(missing_values)
print('\n')

#finding total missing values and percentage of missing values
total_cells=np.prod(permit_data.shape)
total_missing_val=missing_values.sum()

percent_missing=(total_missing_val/total_cells)*100
print(f'The percentage of missing values in the dataset are: {percent_missing}%')
print('\n')

'''remove all rows with a missing value

permit_data.dropna()

'''
#remove all columns with atleast one missing value
columns_w_na_dropped=permit_data.dropna(axis=1)
print('head after dropping columns with atleast one missing value:')
print(columns_w_na_dropped.head())
print('\n')

#finding how much data did we lose
print(f'columns in original dataset: {permit_data.shape[1]}')
print(f'columns after dropping na values: {columns_w_na_dropped.shape[1]}')


