# fruits = ["apple", "banana", "apple", "cherry", "banana"]

# print(type(fruits))

# unique_fruits = set(fruits)

# print(type(unique_fruits))
# print(unique_fruits)

# fruits_list = list(unique_fruits)
# print(type(fruits_list))
# print(fruits_list)

nums = (1, 2, 3, 2, 5, 2, 1, 5, 8)
print(type(nums))
print(nums[2])# at index 2 it should print 3 as the output
print(nums[-1])# at index -1 it will always be the last value in the tuple i.e 8
print(nums[1:3]) # this will provide an output from starting index 1 till 2 i.e 2 , 3

print(nums.count(2))
print(nums.index(2))