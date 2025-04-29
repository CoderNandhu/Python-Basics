### **Mini Project: Customer Purchase System**

# Imagine you're building a **store management system** where you want to track:

# - **Customers** who purchase items.
# - **What they bought**.
# - **The quantity of each item** they bought.


#### **Step 1: Create the data structure**

# You will start with **customer data** that includes **names** and a list of **items** with quantities.

# Example:

# - Alice bought 2 apples, 1 milk, and 1 bread.
# - Bob bought 1 banana and 3 sugars.
# - Charlie bought 5 oils, 2 rice, and 1 flour.

# Here’s the data structure:


orders = [
    {"name": "Alice", "items": {"apple": 2, "milk": 1, "bread": 1}},
    {"name": "Bob", "items": {"banana": 1, "sugar": 3}},
    {"name": "Charlie", "items": {"oil": 5, "rice": 2, "flour": 1}},
]


#### **Step 2: Create the dictionary**

# Create a dictionary where each customer’s name is a **key** and their **purchased items** (with quantities) are the **values**.
customer = {order["name"] : order["items"] for order in orders}
# print(customer)

#### **Step 3: Print details**

# 1. **Print the items purchased by each customer**.
for item in customer.items():
    print(item)

# 2. For each customer, print:
#    - Their **name**.
#    - The **items** they bought (with quantities).
for name, items in customer.items():
    print(f"Item bought by {name}")
    for item, quan in items.items():
        print(f"- {item} : {quan}")

#### **Step 4: Extra Features (Optional)**

# - **Find total quantity of a specific item bought by all customers** (e.g., how many apples in total).
for names, items in customer.items():
    for item, quan in items.items():
        print(f"{item} : {quan}")

# - **Remove a customer** and their purchases.

print(customer.pop(""))
# - **Add a new item** to a customer's purchase.
# - **Update the quantity** of an item.


### **Here’s your task:**
# 1. Create the dictionary with customer names and items bought.
# 2. Print the name and items bought for each customer.
# 3. For the extra challenge:
#    - Add the functionality for **removing** a customer.
#    - Add the functionality for **updating the quantity** of an item.
#    - Add the functionality for **getting the total quantity** of a specific item across all customers.


### **You can start now, and I’m here for any questions.**  
# Once done, let me know, and I’ll review your solution!