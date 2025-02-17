import pandas as pd
import numpy as np
import charset_normalizer
from utils import read

np.random.seed(0)

with open('./datasets/PoliceKillingsUS.csv','rb') as raw_data:
    result=charset_normalizer.detect(raw_data.read(1000000))
print(result)    

police_killings=pd.read_csv('./datasets/PoliceKillingsUS.csv',encoding='windows-1250')

#printing the output
print(police_killings.head())
