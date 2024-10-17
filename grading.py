#Lela Parks
#Oct 15, 2024

# Get exam grades from the user
exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))
exam_three = int(input("Input exam grade three: "))

# Store the grades in a list
grades = [exam_one, exam_two, exam_three]

# Calculate the sum and average
total = sum(grades)
avg = total / len(grades)

# Determine the letter grade
if avg >= 90:
    letter_grade = "A"
elif avg >= 80:
    letter_grade = "B"
elif avg >= 70:
    letter_grade = "C"
elif avg >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Print the results
for grade in grades:
    print("Exam: " + str(grade))

print("Average: " + str(avg))
print("Grade: " + letter_grade)

# Check if the student is passing or failing
if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")

#The input handling exam_two and three should be intigers
#Remember! Intigers are a specific set of whole numbers that can be either positive or negative.
#They lack decimals and fractions with the main purposes of counting, index usage, or for calculations.

#Re-naming was needed for the variables ue to python's built in intigers such as "sum" which has also caused a conflict in the code

#The syntax for "If" statments needed to be re-done and "Print" was missing from the code. Extra characters used in the code where not needed.

#Make sure to spell check your codes before running them in the terminal. That way you will avoid errors and python mistaking your sentences for codes.