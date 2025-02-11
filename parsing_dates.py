import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from utils import read,drop,date_time,plotting

#read the csv file and display head
earthquakes_data=read.read_file('./datasets/earthquakes.csv')

np.random.seed(0)

date_time.check_column_dtype(earthquakes_data,'Date')

date_time.diff_format_check(earthquakes_data,'Date')

#convert into date column to datetime
earthquakes_data.loc[3378, "Date"] = "02/23/1975"
earthquakes_data.loc[7512, "Date"] = "04/28/1985"
earthquakes_data.loc[20650, "Date"] = "03/13/2011"

date_time.convert_to_datetime(earthquakes_data,'date_parsed','Date')

#get the day of the month from the date column
day_of_month_earthquakes=earthquakes_data['date_parsed'].dt.day
print(day_of_month_earthquakes)

#Plot the day of the month to check the date parsing
drop.drop_all_rows(day_of_month_earthquakes)

plotting.histogram(day_of_month_earthquakes,31)







