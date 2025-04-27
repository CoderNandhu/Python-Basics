# Create a dictionary for your favorite book with keys: "title", "author", and "year".
# Then, print each value separately.

book = {
    "title": "Power of subconcious mind",
    "author" : "Dalvick",
    "year": 2010
}

print(book.get("title"))
print(book.get("author"))
print(book.get("year"))


# Create a dictionary for a student: "name", "age", "course".
student = {
    "name": "Alwin",
    "age": 20,
    "course": "ADCD"
}

# Add a new key "grade" with a value.
student["grade"] = "A"
print(student)
# Then, update "age" to a new value.
student.update({"age":21})
print(student)


# Create a dictionary for a car: "brand", "model", "year".
car = {
    "brand": "TATA",
    "model": "Altroz",
    "year":2019
}
# Remove the "year" key using .pop().
car.pop("year")
# Print the dictionary after removal.
print(car)


# Create any dictionary (your choice).
# Use:
fruits = {
    "name": "apple",
    "quantity": 10,
    "expire": 2026
}

# .get() to safely access a key.

print(fruits.get('quantity'))
# .keys()

print(fruits.keys())
# .values()

print(fruits.values())
# .items()

print(fruits.items())



inventory = {"apple": 5, "banana": 8, "orange": 3}
# Update "banana" quantity to 10.
inventory.update({"banana": 10})

# Add a new item "grapes" with quantity 4.
inventory["grapes"] = 4
# Remove "orange" from inventory.
inventory.pop("orange")

# Print the final inventory.
print(inventory)