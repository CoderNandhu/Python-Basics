# Create a tuple named fruits containing "apple", "banana", "cherry", "mango".
fruits = ("apple", "banana", "cherry", "mango")

# Print the first and last elements of the fruits tuple using indexing.
print(fruits[0])
print(fruits[-1])

# Count Occurrence
nums = (1, 2, 3, 2, 2, 4, 5)
print(nums.count(2))

# Unpack this tuple into 3 variables and print them:
person = ("John", 25, "Engineer")
name, age, job = person
print(name)
print(age)
print(job)

# Create a Tuple from a List
colors = ["red", "green", "blue"]
colors_tuple = tuple(colors)
print(colors_tuple)
