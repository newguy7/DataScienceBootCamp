# Write a Python program that takes a list of integers, squares each integer, 
# filters out the squared numbers that are even, and then calculates the sum of the remaining numbers.

import functools

my_list = [1,2,3,2,2,5]

my_sum = functools.reduce(lambda x,y:x+y, filter(lambda x:x % 2==1,map(lambda x:x**2,my_list)))
print(my_sum)