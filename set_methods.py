fruits = {"apple", "banana","mango", "cherry", "grapes"}
# add() ➔ Add one item
fruits.add("guvava")
print(fruits)
# update() ➔ Add multiple items
fruits.update(["orange","pappaya"])
print(type(fruits))
print(fruits)
# remove() and discard() ➔ Remove items
fruits.remove("banana")
print(fruits)
# the difference i noticed with remove and discard is that in remove if the set item is not there it will throw an error 
# but in discard if the item is not there in the set it will not throw an error but it prints the set without an error
fruits.discard("banana")
print(fruits)

# pop() ➔ Remove random item
fruits.pop()
print(fruits)

# clear() ➔ Empty the set
fruits.clear()
print(fruits)

# del ➔ Delete the set completely
del fruits
print(fruits) # this will throw an error as the fruits variable is not there in the memory.