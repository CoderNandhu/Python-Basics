# 🥇 Warmup:
# You have this dictionary:

from traceback import print_tb


student = {
    "name": "Neo",
    "age": 22,
    "subjects": ["Math", "Science", "English"]
}
# ✅ 1. Add a new subject "History" to the subjects list.

subject = student["subjects"].append("Hindi")
print(student["subjects"])

# ✅ 2. Update the student's age to 23.
student.update({"age" : 23})

# ✅ 3. Print all subjects one by one.
for subject in student["subjects"]:
    print(subject)

# ✅ 4. Finally, print the entire updated dictionary.
print(student)