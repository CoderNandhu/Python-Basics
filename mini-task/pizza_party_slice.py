nums_of_pizzas = int(input("Enter the number pizza you have: \n"))

slices_of_pizza = []


for _ in range(nums_of_pizzas):
    for i in range(1,9):
        slices_of_pizza.append(f"pizza{_ + 1} slice{i}")
print(slices_of_pizza)

# list comprehension version

nums_of_pizzas = int(input("Enter the number pizza you have: \n"))

slices_of_pizza = [f"pizza{_ + 1} slice{i}" for _ in range(nums_of_pizzas)
                   for i in range(1,9)]
print(slices_of_pizza)