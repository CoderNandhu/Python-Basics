marks = [90, 85, 78, 92, 88]

students = {}  # empty dictionary

for i in range(len(marks)):
    key = "Student" + str(i+1)  # Student1, Student2, etc.
    students[key] = marks[i]    # Assign marks to student

print(students)