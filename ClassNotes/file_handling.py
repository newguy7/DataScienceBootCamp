# file1 = open('D:/Bootcamp - Data Science/test.txt','r')
# for i in file1:
#     print(i)

# # create a file and write to it
# with open('new_test.txt','w') as fp:
#     fp.write("This is a new file.\n")
#     fp.write("This is the same new file.")
#     fp.close()

# # Read the file
# file1 = open('new_test.txt','r')
# for i in file1:
#     print(i)

# Append to a existing file
with open('new_test.txt','a') as fp:
    fp.write("This is a new file.\n")
    fp.write("This is the same new file.\n")
    fp.close()  

file1 = open('new_test.txt','r')
for i in file1:
    print(i)

# Read email from a text file
def read_emails_from_file(file_path):
    with open(file_path, 'r') as file:
        emails = file.readlines()
    return [email.strip() for email in emails]
