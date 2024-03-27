'''
You are given a dataframe that contains the details about various events in different cities. 
For those cities which start with the keyword ‘New’ or ‘new’, change it to ‘New_’.  
'''
import pandas as pd

data= {
    'City':['New York', 'Parague', 'New Delhi', 'Venice', 'new Orleans'],
    'Event':['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
    'Cost':[10000, 5000, 15000, 2000, 12000]
}

df = pd.DataFrame(data)
# print(df.to_string())

keyword_match = 'New|new'

new_df = df.replace(to_replace=keyword_match, value='New_',regex=True)
print(new_df)

