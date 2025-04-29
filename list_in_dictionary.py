# Create a list of dictionaries of 3 cars.
# Each car has: "brand", "model", and "year".

# Brand: Ford, Model: Mustang, Year: 2015.
# Brand: Toyota, Model: Camry, Year: 2023.
# Brand: BMW, Model: 3 Series, Year: 2025.

# cars = [
#     {"brand" : "ford", "model": "mustang", "year" : 2015},
#     {"brand" : "toyota", "model": "camry", "year" : 2023},
#     {"brand" : "BMW", "model": "3 Series", "year" : 2025}

# ]

# print(cars[1]["brand"])

# ➔ After creating it, print the brand of the second car.


# Task 2
from multiprocessing import Value


employees = [
    {"name": "Alice", "department": "HR", "salary": 50000},
    {"name": "Bob", "department": "Engineering", "salary": 75000},
    {"name": "Charlie", "department": "Marketing", "salary": 60000}
]

worker = {employee["name"] : employee["department"] for employee in employees}
print(worker)
# Your tasks:
# 🔍 Print the name of the person who works in Engineering.
for name, dep in worker.items():
    if dep == "Engineering":
        print(f"The person working in Enginering department is {name}")

# 💸 Print the total salary of all employees.
for i, value in enumerate(employees):
    key = employees[i]["salary"]
    print(key) # i have printed the salary of all employees i don't know if you want the sum of all employees salary


# 📊 Print each employee’s name and salary nicely.
for i, value in enumerate(employees):
    key = employees[i]["salary"]
    worker = employees[i]["name"]
    print(f"{worker} : {key}")


# improved version of this challenge:
# 🔍 Engineering employee
for employee in employees:
    if employee["department"] == "Engineering":
        print(f"{employee['name']} works in Engineering")

# 💸 Total salary
total_salary = sum(emp["salary"] for emp in employees)
print(f"Total salary of all employees: ₹{total_salary}")

# 📊 Name and salary
for emp in employees:
    print(f"{emp['name']} earns ₹{emp['salary']}")
