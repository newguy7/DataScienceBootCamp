'''
Problem Statement:
You are given two lists:
names - a list of names of students.
scores - a list of corresponding scores of the students.
Your task is to create a DataFrame from these lists and perform the following operations:
Create a DataFrame named student_data with columns 'Name' and 'Score'.
Display the first 3 rows of the DataFrame.
Find the average score of all students.
Identify the student with the highest score.
Sort the DataFrame based on the scores in descending order.

'''
import pandas as pd
dataset = {
    "Name":["A","B","C","D"],
    "Score" : [9,7,6,8]
}

student_data = pd.DataFrame(dataset)
#Display the first 3 rows of the DataFrame
#print(student_data.iloc[:3])
print(student_data.head(3))

# Find the average score of all students
average_score = student_data["Score"].mean()
print(f"The average score is: {average_score}")

# Identify the student with the highest score
high_index = student_data["Score"].idxmax()
high_Scorer = student_data["Name"][high_index]
print(f"{high_Scorer} has the highest score.")

# Sort the DataFrame based on the scores in descending order
student_data.sort_values(by="Score",ascending=False,inplace=True)
print("The sorted dataset: ")
print(student_data)