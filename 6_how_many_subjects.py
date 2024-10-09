#
# Adrian
# Calculate average of grades
#

# 1. Input
n_subjects = int(input("How many subjects do you have? "))
subject = []
grade = []

# 2.Process
for i in range(n_subjects):
    subject_name = input(f"Enter name name of subject {i+1}! ")
    subject.append(subject_name)

    subject_grade = int((input(f"Enter grade of subject {i+1}! ")))
    grade.append(subject_grade)
average = sum(grade)/len(grade)

# 3.Output
print(f"Your average is {average}")