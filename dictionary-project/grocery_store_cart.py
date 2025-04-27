# Problem: You are building a grocery cart system!

# ✅ Create a dictionary cart.
cart = {}
# ✅ Add "rice", "oil", "sugar" with quantities 2, 1, and 5.
cart["rice"] = 2
cart["oil"] = 1
cart["sugar"] = 5

# ✅ Update "oil" quantity to 2.
cart.update({"oil":2})
# ✅ Remove "sugar" from the cart.
cart.pop("sugar")
# ✅ Print all items with quantities.
print(cart.items())