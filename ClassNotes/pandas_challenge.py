import pandas as pd
import numpy as np

'''
You are given a Pandas DataFrame containing some missing values (NaNs). Write a function called
clean_empty_values()
that takes a DataFrame as input and replaces all the missing values with a specified default value.
'''

data = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': [np.nan, 10, 11, 12]
}

# create a dataframe
df = pd.DataFrame(data)
print(df.to_string())

def clean_empty_values(data_frame):    
    data_frame.fillna(0,inplace=True)

clean_empty_values(df)
print("After replacing the missing values...")
print(df.to_string())