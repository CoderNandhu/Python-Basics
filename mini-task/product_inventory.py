from operator import mul


products = [
    {"name": "Laptop", "price": 60000, "stock": 5},
    {"name": "Smartphone", "price": 30000, "stock": 10},
    {"name": "Tablet", "price": 20000, "stock": 7}
]

# ✅ Your Tasks:
# 🔍 Print the name and price of all products.
for product in products:
    print(f"Name of the product {product['name']} and price {product['price']}")

# 💰 Calculate the total value of stock for each product (price × stock) and print it.

tota_product_value  = mul(product["price"], product["stock"])
print(f"the total value of stock for each product {tota_product_value}")

# 📦 Calculate and print the grand total value of all products in stock.
total_value  = sum(product['stock'] for product in products)
print(f"the grand total value of all products in stock is {total_value}")
# ✏️ Update the stock of "Laptop" to 4.

products[0].update({"stock" : 4})
print(products)


# updated Code  
from operator import mul

products = [
    {"name": "Laptop", "price": 60000, "stock": 5},
    {"name": "Smartphone", "price": 30000, "stock": 10},
    {"name": "Tablet", "price": 20000, "stock": 7}
]

# ✅ 1. Print the name and price of all products.
for product in products:
    print(f"Name of the product {product['name']} and price {product['price']}")

print()

# 💰 2. Calculate the total value of stock for each product (price × stock) and print it.
for product in products:
    total_product_value = mul(product["price"], product["stock"])
    print(f"Total stock value for {product['name']} = {total_product_value}")

print()

# 📦 3. Calculate and print the grand total value of all products in stock.
grand_total = sum(mul(product["price"], product["stock"]) for product in products)
print(f"Grand total value of all products = {grand_total}")

print()

# ✏️ 4. Update the stock of "Laptop" to 4.
products[0].update({"stock": 4})
print("Updated Products:", products)
