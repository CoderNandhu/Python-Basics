# This is real-world-mini project to practice dictionary in python

# Create an empty dictionary called cart.

cart = {

}

# Add the following items with their quantities:
cart["apple"] = 2
cart["banana"] = 5
cart["milk"] = 1
print(type(cart))
print(cart)

# "apple": 2

# "banana": 5

# "milk": 1

# Update the quantity of "banana" to 7.
cart.update({"banana":7})

# Add a new item "bread" with quantity 2.
cart["bread"] = 2
# Remove "milk" from the cart.
cart.pop("milk")
# Print all items and their quantities (hint: .items()).
print(cart.items())
# Check if "bread" exists in the cart (hint: 'bread' in cart).
print(f"{cart.get("bread")} Bread is in the cart") # first method 

for i in cart:
    if i == "bread":
        print("bread is in the cart")
    else:
        print("bread is not in the cart") # in this method i have noticed that it iterate it finds bread but the else statement is printed twice.
# Safely get the quantity of "orange" without error even if it's not present (hint: .get()).
print(f"{cart.get("orange")} , There is no orange in the cart")


# Check if "bread" exists in the cart (hint: 'bread' in cart).
if cart.get("bread") == True:
    print("Bread is in the cart")
else:
    print("bread is not in the cart") # in this code i have notice that if the value of bread is 1 it says true.