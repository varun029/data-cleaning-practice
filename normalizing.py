import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from utils import read
from scipy import stats
from utils import scale

np.random.seed(0)

#read the file
kickstarter_data=read.read_file('./datasets/ks-projects-201801.csv')

# get the index of all positive pledges (Box-Cox only takes positive values)
index_positive_pledges=kickstarter_data.pledged > 0

# get only positive pledges (using their indexes)
positive_pledges=kickstarter_data.pledged.loc[index_positive_pledges]

#normalize the data
normalized_data=pd.Series(stats.boxcox(positive_pledges)[0],name='pledged',index=positive_pledges.index)

#plot the normalized data
ax = sns.histplot(normalized_data, kde=True)
ax.set_title("Normalized data")
plt.show()






