#Step 1: Load the dataset
#First, we'll load the Titanic dataset. If you have the dataset in a CSV file, we can load it using pandas.


import pandas as pd

# Load dataset
data = pd.read_csv('titanic.csv')
data.head()