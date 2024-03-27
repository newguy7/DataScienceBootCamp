import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import sys

class Stock_Analysis:

    def __init__(self,stock1):
        self.stock1 = stock1
        self.df_stock = None

    # Fetch stock data from yahoo finance and preprocess any missing value
    def get_data(self,start_date,end_date):
        try:
            self.df_stock = yf.download(self.stock1, start=start_date, end=end_date) 

            if len(self.df_stock) == 0:
                print(f"No data found for {self.stock1}. Try appropriate stock symbol.")
                # Exit the program
                sys.exit()                
            
            # check for missing values
            check_nan = self.df_stock.isna().values.any()
            if check_nan:
                self.df_stock.fillna(0,inplace=True)
            print(f"-----------Gathering stock data for {self.stock1}--------------")
            print(self.df_stock)                
            
        except Exception as ex:
            print(f"Error in getting data: {ex}")

    # get all the relevant information available on the stock
    def relevant_info(self):
        try:
            get_stock_info = yf.Ticker(self.stock1)
            
            if get_stock_info is not None:
                print(f"Here are some relevant information on '{self.stock1}'\n")        
                relevant_key = ['longName','website','industry','previousClose','currentPrice',
                                'fiftyTwoWeekLow','fiftyTwoWeekHigh','volume','mostRecentQuarter','fiveYearAvgDividendYield']
                for key in relevant_key:
                    if key in get_stock_info.info:                                         
                        print(key, ":", get_stock_info.info[key])
            else:
                print("No data available!!!")
                # Exit the program
                sys.exit() 
        except Exception as ex:
            print(f"Error in getting data: {ex}")

    # store the data fetched from yahoo finance
    # df_stock = get_data()

    # Calculate 7 days moving  average
    def get_moving_average(self,window):
        if self.df_stock is not None:
            self.df_stock['Moving Average'] = self.df_stock.Close.rolling(window=window).mean()
            # check for missing values
            check_nan = self.df_stock['Moving Average'].isna().values.any()
            if check_nan:
                self.df_stock['Moving Average'].fillna(0,inplace=True)       
            
        else:
            print("No data available!!!")

    # Calculate standard deviation
    def get_std_deviation(self,window):
        if self.df_stock is not None:
            self.df_stock['Std_Deviation'] = self.df_stock['Adj Close'].rolling(window=window).std()
            # check for missing values
            check_nan = self.df_stock['Std_Deviation'].isna().values.any()
            if check_nan:
                self.df_stock['Std_Deviation'].fillna(0,inplace=True)
        else:
            print("No data available!!!")
    
    # Calculate daily returns
    def daily_exp_risk(self):
        daily_returns = self.df_stock['Adj Close'].pct_change().dropna()
        
        # Calculate expected return (average of daily returns)
        expected_return = daily_returns.mean()
        
        # Calculate risk (standard deviation of daily returns)
        risk = daily_returns.std()
    
        return expected_return,risk

    # Calculate correlation coefficient between two stocks
    def get_corr_coefficient(self,stock_to_compare,start_date,end_date):        
        try:            
            stock2_data = yf.download(stock_to_compare, start=start_date, end=end_date)            
            correlation = self.df_stock['Close'].corr(stock2_data['Close'])            
            print(f"Correlation coefficient between {self.stock1} and {stock_to_compare}: {round(correlation,2)}")
            if (correlation == 1):
                print(f"There is a Perfect Positive Correlation between {self.stock1} and {stock_to_compare}")
            elif (0.6 <= correlation < 1):
                print(f"There is a Strong Positive Correlation between {self.stock1} and {stock_to_compare}")
            elif (0 < correlation < 0.6):
                print(f"There is a Weak Positive Correlation between {self.stock1} and {stock_to_compare}")
            elif (correlation == -1):
                print(f"There is a Perfect Negative Correlation between {self.stock1} and {stock_to_compare}")    
            elif (-1 < correlation < -0.6):
                print(f"There is a Strong Negative Correlation between {self.stock1} and {stock_to_compare}")
            elif (-0.6 < correlation < 0):
                print(f"There is a Weak Negative Correlation between {self.stock1} and {stock_to_compare}")
            elif (correlation == 0):
                print(f"There is No correlation between {self.stock1} and {stock_to_compare}")
        except Exception as e:
            print(f"Error calculating correlation coefficient: {e}")

    def get_updated_data(self):
        print('\n')
        print(f"Gathering additional information on {self.stock1} ..........")
        print(self.df_stock.to_string())

    def plot_data(self):
        # Plot stock data
        if self.df_stock is not None:
            self.df_stock['Close'].plot(figsize=(10, 6))
            plt.title(f"{self.stock1} Stock Price")
            plt.xlabel("Date")
            plt.ylabel("Price (USD)")
            plt.grid(True)
            plt.show()
        else:
            print("No data available for plotting.")
    
    def plot_moving(self,window):        
        if self.df_stock is not None:
            self.df_stock['Moving Average'].plot(figsize=(10, 6))

            plt.title(f"{self.stock1} {window} day Moving Average")
            plt.xlabel("Date")
            plt.ylabel("Price (USD)")
            plt.grid(True)
            plt.show()
        else:
            print("No data available for plotting.")
    
    def scatter_plot(self):        
        if self.df_stock is not None:
            x = self.df_stock['Moving Average']
            y = self.df_stock['Std_Deviation']
            plt.title(f"Scatter Plot")
            plt.xlabel("Moving Average")
            plt.ylabel("Standard Deviation")
            plt.grid(True)
            plt.scatter(x,y)
            plt.show()
        else:
            print("No data available for plotting.")

