# write a program to print each word of the line using print function

# Read each word of the line
with open('./test.txt','r') as file1:
    for line in file1:
        for word in line.split():
            print(word)
