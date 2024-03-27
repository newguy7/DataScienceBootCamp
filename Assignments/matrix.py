# Write a Python program that generates a list of tuples representing all possible pairs 
# of numbers from two given lists, and filters out pairs where the sum of the numbers is divisible by 3

list1 = [1,2,3,4,5]
list2 = [2,3,5,6]

new_list = [(i, j) for i in list1 for j in list2 if (i + j) % 3 != 0]
print(new_list)

