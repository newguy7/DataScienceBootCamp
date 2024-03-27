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