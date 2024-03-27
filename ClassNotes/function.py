# def func2(X:int, Y:int) -> int :
#     print(X)
#     print(Y)
#     return X, Y

# value_func = func2(2,"hello")

# print(value_func)

# x,y = value_func
# print(x)

# (x,y) = (2,3)

"""
You are given a list of integers representing the prices of stock on consecutive days. You need to design a Python function
max_profit
to find the maximum profit you can make from buying and selling stocks at most once. 
Your function should take a list of integers representing the prices as input and 
return an integer representing the maximum profit. If it's not possible to make a profit, return 0.

prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))  # Output should be 5 (Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5)

"""

# def max_profit(prices):
#     if not prices:
#         return 0
    
#     min_price = prices[0]
#     max_profit = 0

#     for price in prices:
#         min_price = min(min_price,price) # update the minimum price

#         # calculate maximum profit if we sell at current price
#         # then update maaximum profit
#         max_profit = max(max_profit, price - min_price)
#     return max_profit

# stock_prices1 = [7, 1, 5, 3, 6, 4]
# print(max_profit(stock_prices1))

# stock_prices2 = [7, 2, 5, 1, 6, 4]
# print(max_profit(stock_prices2))

# stock_prices3 = [7, 3, 5, 3, 6, 1]
# print(max_profit(stock_prices3))

# stock_prices4 = [7, 2, 5, 3, 1, 4]
# print(max_profit(stock_prices4))

# def func4(**kwargs):    
#     for key,value in kwargs.items():
#         print(f"{value}")
# func4(a=5,b=4,c=6)

# def func5(*args):
#     print("Printing values")
#     for x in args:
#         print(x)

# func5(3,4,'5')
# func5(20, 40, 60)
# func5(80, 100)

# def calculation(a,b):
#     add_values = a + b
#     sub_values = a - b
#     return add_values, sub_values

# res = calculation(40,10)
# print(res)

# add,sub = calculation(40,10)
# print(add, sub)

# def show_employee(name,salary=9000):
#     print(f"Name: {name} Salary: {salary}")

# show_employee("Ben",12000)
# show_employee("Jessa")

'''
Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it
'''
# def out_func1(a,b):
#     def in_func(a,b):
#         return a + b

#     add = in_func(a,b)
#     return add + 5

# result = out_func1(5,10)
# print(result)

'''
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
'''
# def recur_func(n):
#     sum1 = 0
#     for x in range(n):
#         sum1 += x
#     return sum1

# print(recur_func(11))

'''
Assign a different name to function and call it through the new name
'''
# def display_student(name,age):
#     print(name,age)

# # call using original name
# display_student("Emma", 26)

# # assign new name
# show_student = display_student
# # call using new name
# show_student("Emma", 26)

'''
Generate a Python list of all the even numbers between 4 to 30
'''
# def gen_even_list():    
#     even_list = [x for x in range(4,30) if x%2==0]
#     return even_list

# print(gen_even_list())

# #alternative
# print(list(range(4,30,2)))

# Find the largest item from a given list
x1 = [4, 6, 8, 24, 12, 2]
print(max(x1))

# Alternatively
from functools import reduce
print(reduce(lambda x,y : x if x>y else y,x1))