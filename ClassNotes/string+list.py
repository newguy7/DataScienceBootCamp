# print("The sum of 1 + 2 is {0} and {2}".format("1+2","2+3",3+4))

# num1 = int(input("enter a number: "))
# num2 = int(input ("enter second number: "))
# sum = num1+num2

# print("The sum of {0} and {1} is {2}".format(num1, num2, sum))

# import array as arr

# a = arr.array('i', [1,2,3,4,5,6])
# print(a[0])
# print(a[3])

list1 = [1,2,3,2,0,2]

list2 = [4]
list2.extend(list1)

# print(list2)

# list1.remove(2)
# print(list1)

# list1.pop(1)
# print(list1)

# list1.reverse()
# print(list1)

# print(list1.index(2,2))

# print(list1.count(2))

# list1.sort(reverse=False) #default ascending
# print(list1)

list3 = list1.copy()
list3.append(12)
print(list3)
print(list1)

list4 = list1
list1.append(99)
print(list4)
print(list1)