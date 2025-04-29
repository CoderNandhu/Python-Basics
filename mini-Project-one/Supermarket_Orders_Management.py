# Scenario:
# You are building a system for a supermarket to manage customer orders.

# Each customer has:

# A name (string)

# A list of items they bought (list of strings)

# Your Tasks:
# ✅ 1. Create a list of dictionaries.
# Each dictionary should represent one customer with their name and list of items.

# ✅ 2. Print the name of each customer.

# ✅ 3. For each customer, print all items they bought one by one.




orders = [
    {"name": "Alice", "items": ["apple", "milk", "bread"]},
    {"name": "Bob", "items": ["banana", "sugar"]},
    {"name": "Charlie", "items": ["oil", "rice", "flour", "salt"]}
]

# print(orders)
customer = {order["name"] : order["items"] for order in orders}

print(customer)

for name in customer:
    print(name) # printing name of each customer

# alice_item = customer["Alice"]
# print(alice_item)

# for name, items in customer.items():
#     print(f"Items bought by {name}")
#     for item in items:
#         print(f"- {item}")
#     print()