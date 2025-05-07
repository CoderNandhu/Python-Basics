students = {
    "Alice": {"math": 90, "science": 85},
    "Bob": {"math": 78, "science": 92},
    "Charlie": {"math": 88, "science": 79}
}

# Print Alice’s science score
# for name, scores in students.items():
#     print(f"{name}'s Score")
#     for subject, score in scores.items():
#         print(f" - {subject}: {score}")
student = students["Alice"]["science"]
print(student)

# Print each student's name and their total score (math + science)
for name, scores in students.items():
    print(f"{name}'s Score")
    for subject, score in scores.items():
        print(f" - {subject}: {score}")

    total_score = scores["math"] + scores["science"]
    print(f"Total Score obtain is {total_score}")

# for name, scores in students.items():
#     print(f"{name}'s Scores:")
#     for subject, score in scores.items():
#         print(f" - {subject}: {score}")
#     total = scores["math"] + scores["science"]
#     print(f" ➤ Total: {total}\n")

        
        # print(f"total score is : {total_score} ")

# Add a new subject "English" with scores (you can make up values)
students["Alice"].update({"english" : 65})
students["Bob"].update({"english" : 70})
students["Charlie"].update({"english" : 89})


# Print the updated dictionary
print(students)