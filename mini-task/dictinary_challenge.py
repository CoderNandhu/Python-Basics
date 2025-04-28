
# ✅ Create a dictionary where:

# Keys = "Fruit1", "Fruit2", "Fruit3", "Fruit4"

# Values = the actual fruit names.

# ✅ Expected Output:
# {
#     "Fruit1": "apple",
#     "Fruit2": "banana",
#     "Fruit3": "mango",
#     "Fruit4": "grapes"
# }
fruits = ["apple", "banana", "mango", "grapes"]

fruit = {}

for i, value in enumerate(fruits):
    key = "fruit"+ str(i +1)
    print(key)
    fruit[key] = fruits[i]

print(fruit)