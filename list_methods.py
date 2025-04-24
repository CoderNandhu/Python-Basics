# Method	What it does
# append()	Add an item to the end
# insert()	Add an item at a specific position
# remove()	Remove the first occurrence of an item
# pop()	    Remove item at a specific index (or last if index not given)
# sort()	Sort the list
# reverse()	Reverse the list
# clear()	Remove all items from the list

items = [1, "Apple", 2, "orange", 3, "grapes"]

print(type(items))
print(items)
print(id(items))

# lets start whith diffrent list methods:

items.append([4, "mango"])
print(items)
print(id(items))

items.append(5)
items.append("cherry")
print(items)
print(id(items))


items.insert(0, 0)
items.insert(1,"pappaya")
print(items)
print(id(items))

items.pop(8)
items.pop()
items.pop()
items.remove(0)
print(items)
print(id(items))

items.sort(key=lambda x: str(x))
print(items)
print(id(items)) # to identify the id in the memory location 
# which makes it clear that the list has been modified and it is mutable and the new list is not created like string

num = [1, 2, 3, 4, 5]
num.reverse()
print(num)
print(id(num))

items.clear()
print(items)
print(id(items))