# Student Grade Calculator

# Ask the user to enter the student's name
# (If no name is entered, the code will not continue)
name = input("Enter student's name: ")

# Create an empty list to store the marks of 5 subjects
marks = []

# Use a for loop to get marks for 5 subjects from the user
for i in range(5):
    mark = float(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(mark)

# Calculate the average of all the marks
average = sum(marks) / len(marks)

# Decide the grade based on the average marks
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 60:
    grade = 'C'
else:
    grade = 'D'

# Display the final result
print("\nStudent: " + name)
print("Average Marks: " + str(round(average, 2)))
print("Grade: " + grade)
