# mini project 

inventory = {"apple": 10, "banana": 5}

# Add oranges
inventory["orange"] = 8

# Update apples
inventory["apple"] = 12

# Remove bananas
inventory.pop("banana")

print(inventory)  # {'apple': 12, 'orange': 8}

for key, value in inventory.items():
    print(key, value)