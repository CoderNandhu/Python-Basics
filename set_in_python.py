# Create a set:

# fruits = {"apple", "banana", "cherry"} using {}.

# numbers = [1, 2, 3, 2, 1, 4] and convert it into a set using set().

fruits = {"apple", "banana", "cherry"}
print(type(fruits))
print(fruits)

numbers = [1, 2, 3, 2, 1, 4] #list

numbers_con = set(numbers) # converting list into set
print(numbers_con) # printing the list after converting
# you can see the changes in the output area all the duplicate values are removed the output is {1, 2, 3, 4}