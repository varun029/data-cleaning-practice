import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from utils import read
from utils import date_time

#read the csv file and display head
earthquakes_data=read.read_file('./datasets/earthquakes.csv')

np.random.seed(0)

#check data type of date column
print(earthquakes_data['Date'].head())
print('\n')

#checking the length of each entry in the "Date" column
date_lengths = earthquakes_data.Date.str.len()
print(date_lengths.value_counts())
print('\n')

#obtain the indices corresponding to rows which are in a diff format and print the data
indices=np.where([date_lengths==24])[1]
print('Indices with corrupted data:', indices)
print(earthquakes_data.loc[indices])

#convert into date column to datetime
earthquakes_data.loc[3378, "Date"] = "02/23/1975"
earthquakes_data.loc[7512, "Date"] = "04/28/1985"
earthquakes_data.loc[20650, "Date"] = "03/13/2011"
earthquakes_data['date_parsed'] = pd.to_datetime(earthquakes_data['Date'], format="%m/%d/%Y")

#get the day of the month from the date column
day_of_month_earthquakes=earthquakes_data['date_parsed'].dt.day
print(day_of_month_earthquakes)

#Plot the day of the month to check the date parsing
day_of_month_earthquakes=day_of_month_earthquakes.dropna()
sns.histplot(day_of_month_earthquakes,kde=False,bins=31)
plt.show()






