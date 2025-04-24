# Imagine you're organizing two online store sales:

# Sale_A customers bought: {"Alice", "Bob", "Charlie", "David"}

# # Sale_B customers bought: {"Charlie", "David", "Eva", "Frank"}

# Customers who bought in both sales (intersection).

# Customers who bought in only one sale (symmetric_difference).

# Customers who bought in only Sale_A but not Sale_B (difference).

# Whether both sales had completely different customers (isdisjoint).

# Is Sale_A a subset of Sale_B?

sale_a = {"Alice", "Bob", "Charlie", "David"}
sale_b = {"Charlie", "David", "Eva", "Frank"}

# 1. Customers in both sales
print(f"The Customer who bought in same sales are: {sale_a.intersection(sale_b)}")

# 2. Customers in only one sale
print(f"The customer only in one sale is : {sale_a.symmetric_difference(sale_b)}")

# 3. Customers only in Sale_A
print(f"The customer only bought in sale_a {sale_a.difference(sale_b)}")

# 4. Are sales completely different?
print(f"Is the sale is completely different :{sale_a.isdisjoint(sale_b)}")

# 5. Is Sale_A a subset of Sale_B?
print(f"sale a is subset of sale b : {sale_a.issubset(sale_b)}")
