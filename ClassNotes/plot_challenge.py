'''
Challenge: Plotting COVID-19 Cases
Objective:Visualize the daily COVID-19 cases from a given dataset.
Instructions:
Download a dataset containing daily COVID-19 cases. You can use online sources like Kaggle or government health websites for this purpose.
Load the dataset into a Pandas DataFrame.
Preprocess the data if necessary (e.g., handle missing values, convert data types).
Plot the daily COVID-19 cases over time.
Customize the plot with appropriate titles, labels, and styles.
Save the plot as an image file.
'''

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

# create dataset
# #covid_dataset = pd.read_csv("covid19_data.csv")
covid_dataset = pd.read_csv(url)

# checking for null value
missing_value = covid_dataset.isna().values.any()

# preprocessing the data
if missing_value:
    clean_df = covid_dataset.fillna(0)
# print(clean_df)
# aggregate the data by date and sum across countries
df_agg = clean_df.drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
# print(df_agg.to_string())


# # Plot the daily COVID-19 cases over time
# df_agg.plot(kind='line', marker='o', color='b', linestyle='-')

# plt.xticks(fontsize=12)
# plt.title('Global Daily COVID-19 Cases')
# plt.xlabel('Date',fontsize=14)
# plt.ylabel('Number of cases',fontsize=14)
# plt.grid(True)


# # #Save the plot as an image file
# plt.savefig('output.png')

# # Display the plot
# plt.show()

'''
Implement at least two of the following additional tasks:
A. Compare COVID-19 statistics (cases, deaths, recoveries) between different countries or regions.
B. Calculate and visualize rolling averages to smooth out daily fluctuations.
C. Plot additional relevant information such as testing rates, vaccination rates, or hospitalization rates.
'''

url_confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url_deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
url_recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

# Create dataframe
df_confirmed = pd.read_csv(url_confirmed)
df_deaths = pd.read_csv(url_deaths)
df_recovered = pd.read_csv(url_recovered)

# Set display options to show floats with 2 decimal places
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# calcualte sum of confirmed cases, deaths and recovered
total_confirmed = df_confirmed.drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum(axis=1)
total_deaths = df_deaths.drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum(axis=1)
total_recovered = df_recovered.drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum(axis=1)

# Insert total cases, deaths, and recovered columns into df_confirmed DataFrame
df_confirmed.insert(2,"Total_cases",total_confirmed,True)
df_confirmed.insert(3,"Total_deaths",total_deaths,True)
df_confirmed.insert(4,"Total_recovered",total_recovered,True)

# Compare COVID-19 statistics (cases, deaths, recoveries) between different countries or regions.
selected_columns = ['Country/Region','Total_cases','Total_deaths','Total_recovered']
check_missing_value = df_confirmed.isna().values.any()
if check_missing_value:
    df_confirmed.fillna(0,inplace=True)

# show the statistics
df_grouped = df_confirmed[selected_columns].groupby("Country/Region").sum()
# print(df_grouped.to_string())

# calcualte rolling mean
clean_df.drop(['Province/State','Country/Region','Lat','Long'],axis=1).dropna(inplace=True)

print(clean_df.rolling(7).mean().head(10))

# plt.plot(df_confirmed["Country/Region"],df_confirmed["Total"])

# plt.xticks(fontsize=12)
# plt.title('Global COVID-19 Cases')
# plt.xlabel('Country/Region',fontsize=14)
# plt.ylabel('Total cases',fontsize=14)
# plt.grid(True)


# # # #Save the plot as an image file
# plt.savefig('output.png')

# # # Display the plot
# plt.show()