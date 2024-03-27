# def starts_with_A(s):
#    return s[0] == 'A'

# #MAP function
# fruit = ['Apple', 'Banana']
# map_object = map(starts_with_A, fruit)
# print(list(map_object))

# #filter function
# filter_object = filter(starts_with_A, fruit)
# print(list(filter_object))

# filter_list = filter(lambda x:x[0]=='A',fruit)
# print(list(filter_list))


# temp_c = [32,44,60,98]
# def conv_to_f(tempc):
#     temp_F = []
#     for temp in tempc:
#         f = (temp * 9/5) + 32
#         temp_F.append(f)    
#     return temp_F


# # using map and lambda
# temp_f = map(lambda x:x * (9/5) + 32, temp_c)
# print(list(temp_f))

# PYTHON PROGRAM THAT TAKES A LIST OF STRINGs AND FILTER OUT THE STRINGS THAT HAVE A LENGTH < 5
# string_list = ['hello', 'Hi', 'welcome', 'it is cold today', 'Nice']
# filter_string = filter(lambda x:len(x) < 5,string_list)
# print(list(filter_string))

#Reduce function
"Write a Python program that takes a list of numbers and finds the maximum number using the reduce() function."
import functools

# list1 = [1,2,3,34,18,72,6]
# max_num = functools.reduce(lambda num1,num2:max(num1,num2),list1)
# max_num_1 = functools.reduce(lambda num1,num2:num1 if num1 > num2 else num2,list1)
# print(max_num)
# print(max_num_1)

# list_2 = [1,2,3]
# # sum of squares of all numbers in the list
# my_sum = functools.reduce(lambda x,y: x**2+y,list_2) # ??
# print(my_sum)

# Write a Python program that takes a list of integers, squares each integer, 
# filters out the squared numbers that are even, and then calculates the sum of the remaining numbers.

my_list = [1,2,3,2,2,5]

my_sum = functools.reduce(lambda x,y:x+y, filter(lambda x:x % 2==1,map(lambda x:x**2,my_list)))
print(my_sum)






    