import seaborn as sns
import matplotlib.pyplot as plt

def histogram(df,x):
    sns.histplot(df,kde=False,bins=x)
    plt.show()