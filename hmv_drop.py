'''
Steps to handle missing values
1. Take a first look at the data
2. How many missing data points do we have?
3. Figure out why data is missing
4. Drop missing values / Filling in missing values
'''

import numpy as np
from utils import read
from utils import missing
from utils import drop
from utils import columns_drop_summary

#reading the csv file
permit_data=read.read_file('./datasets/Building_Permits.csv')

#set seed for reproductibility
np.random.seed(0)

#finding missing values per column
missing_vals=missing.miss_val_column(permit_data)

#finding total missing values and percentage of missing values
percent_missing=missing.miss_val_percentage(permit_data,missing_vals)

#remove all columns with atleast one missing value
columns_w_na_dropped=drop.drop_column(permit_data)

#finding how much data did we lose
columns_drop_summary.compare_column_count(permit_data,columns_w_na_dropped)

