'''
Write a Python function sum_of_even(arr) that takes a 1-dimensional NumPy array arr as input 
and returns the sum of all even numbers in the array.
Here are the specifications:
The function should return 0 if there are no even numbers in the array.
You can assume that the input array arr will contain only integers.
'''
import numpy as np

# using normal way
def sum_of_even(arr):  
               
    if np.array(arr).ndim == 1:
        sum1 = 0
        for x in arr:
            if x%2==0:
                sum1+= x
            else:
                return 0
        return sum1
    else:
        print("Provide 1-dimensional NumPy array as input ")
    

# arr1 = [1,2,3,4,5,6]
# print(sum_of_even(arr1))

# using filter&lambda function
def sum_of_even(arr):
    if np.array(arr).ndim == 1:        
        return sum(filter(lambda x:x if x % 2 == 0 else 0, arr))        
    else:
        print("Provide 1-dimensional NumPy array as input ")
        

arr1 = [1,3,4,5,6]
# print(sum_of_even(arr1))

# Reverse Array
'''
Write a Python function reverse_array(arr) that takes a 1-dimensional NumPy array arr as input 
and returns a new array containing the elements of arr in reverse order.
Here are the specifications:
The function should return a new array with the elements of arr reversed.
You should not modify the original array arr.
You can assume that the input array arr will contain only integers.
'''

def reverse_array(arr):
    arr = np.array(arr)
    new_arr = np.copy(arr)[::-1]
    print(arr)
    return new_arr

# print(reverse_array([1,2,3,4]))

# Challenge: Random Array Generation
'''
Write a Python function generate_random_array(shape, low, high) 
that generates a NumPy array of a specified shape filled with random numbers within a given range.

Here are the specifications:
shape is a tuple representing the shape of the array to be generated.
low and high are the lower and upper bounds of the range of random numbers to be generated, inclusive.
The function should return a NumPy array with the specified shape containing random numbers within the specified range.
You can assume that low will always be less than or equal to high.
'''
from numpy import random

def generate_random_array(shape, low, high):
    if isinstance(shape, tuple):
        return  random.randint(low,high+1,size=shape)
    else:
        print("Shape should be passed as a tuple")

print(generate_random_array((2,3),10, 20))
