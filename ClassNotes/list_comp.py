"Write a program to print a list with all numbers less than 100 who are divisible by both 2 and 5?"

def div_by_2_and_5():
    my_list = [x for x in range(100) if x%2 == 0 and x%5 == 0]
    return my_list

print(div_by_2_and_5())