# write a program to print each word of the line using print function. 

# create a file and write to it
with open('new_test1.txt','w') as fp:
    fp.write("This is a test file.\n")
    fp.write("This is the same test file.")
    fp.close()

# Read each word of the line
# file1 = open('new_test1.txt','r')
# for line in file1:    
#     for word in line.split():
#         print(word)


# Write a Python program that reads data from a text file 
# containing the names and ages of individuals, calculates the average age, 
# and writes the names of individuals whose age is above the average to a new text file.
        
# Read data from the text file
with open('individuals.txt', 'r') as file:
    lines = file.readlines()
 
# Extract names and ages
names = []
ages = []
for line in lines:
    name, age = line.strip().split(',')
    names.append(name)
    ages.append(int(age))
 
# Calculate average age
average_age = sum(ages) / len(ages)
 
# Filter names of individuals above average age
above_average_names = []
for i in range(len(names)):
    if ages[i] > average_age:
        above_average_names.append(names[i])
 
# Write names to a new text file
with open('above_average_names.txt', 'w') as file:
    for name in above_average_names:
        file.write(name + '\n')
 
print("Names of individuals above average age saved to 'above_average_names.txt'")


