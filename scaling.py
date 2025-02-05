import pandas as pd 
import numpy as np
from utils import read
from utils import scale

np.random.seed(0)

#reading the csv file
kickstarter_data=read.read_file('./datasets/ks-projects-201801.csv')

# selecting the column to be scaled
kickstarter_data=pd.DataFrame(kickstarter_data.usd_goal_real)

#scaling the data
kickstarter_scaled=scale.minmax(kickstarter_data,'usd_goal_real')

#comparing scaled data and unscaled data
scale.compare_data(kickstarter_data,kickstarter_scaled)



