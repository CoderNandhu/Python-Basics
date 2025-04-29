# You are building a system for a pizza shop.
# You have a list of pizza types ordered by customers:
# ✅ Task 1:
# Create a dictionary where keys are "order1", "order2", etc., and values are the pizza names.

# ✅ Task 2:
# Print the final dictionary.

# ✅ Bonus Task:
# Print only the pizza names (values) one by one from the dictionary.

# expected output 
# {
#     "order1": "Margherita",
#     "order2": "Pepperoni",
#     "order3": "Veggie",
#     ...
# }

pizzas = ["Margherita", "Pepperoni", "Veggie", "Margherita", "Pepperoni", "BBQ Chicken"]

pizza = {} # created empty dictionary

for i, value in enumerate(pizzas):
    key = "order" + str(i+1)
    # print(key)
    pizza[key] = value
print(pizza)

print(pizza.values())