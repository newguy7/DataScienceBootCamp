'''
Create a list by picking an odd-index items from the first list and even index items from the second
'''

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l3 = []

for num in l1:
    if l1.index(num)%2==1:
        l3.append(num)

for num in l2:
    if l2.index(num)%2==0:
        l3.append(num)

print(l3)

