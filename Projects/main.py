from stock_data import Stock_Analysis
import datetime as dt

def run_analysis():

    # Ask user to enter the stock to analyse
    user_stock = input("Please enter a stock symbol: ").upper()

    # define start and end date
    start_date = dt.datetime(2024,2,1)
    end_date = dt.datetime.today()
    window = 7

    # create the object of Stock Analysis Class
    stock_analysis = Stock_Analysis(user_stock)

    # Show relevant information of the stock
    stock_analysis.relevant_info()  

    # Fetch data for user input stock
    stock_analysis.get_data(start_date=start_date,end_date=end_date)    

    # Plot stock data
    stock_analysis.plot_data()  

    # Calculate moving average with a window of 30 days
    stock_analysis.get_moving_average(window=window)

    # Plot moving average
    stock_analysis.plot_moving(window=window)

    # Calculate standard deviation with a window of 30 days
    stock_analysis.get_std_deviation(window=window)    

    # show updated data on the stock - moving average and standard deviation included
    stock_analysis.get_updated_data()

    # plot scatter diagram
    stock_analysis.scatter_plot()

    # calculate expected return and risk
    expected_return, risk = stock_analysis.daily_exp_risk()
    print("**********************************************")
    print(f"Expected return of {user_stock}: {expected_return:.4f}")
    print(f"Risk (standard deviation) of {user_stock}: {risk:.4f}")

    # Calculate correlation coefficient with another stock
    print('\n')
    print("Calculate correlation coefficient with another stock.... ")
    stock2 = input(f"Please enter another stock symbol to compare with {user_stock}: ").upper()
    stock_analysis.get_corr_coefficient(stock_to_compare=stock2,start_date=start_date,end_date=end_date)

if __name__ == "__main__":
    run_analysis()

    