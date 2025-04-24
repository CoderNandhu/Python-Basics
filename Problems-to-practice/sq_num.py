nums = [i for i in range(10)]
print(nums)

nums = []

for i in range(10):
    num = i * i
    nums.append(num)
print(nums)

nums = [i * i for i in range(10)]
print(nums)

# program to create a list using list comprehension only for even nums from 0 - 19

nums = []

for i in range(20):
    if i % 2 == 0:
        nums.append(i)
print(nums)

nums = [i for i in range(20) if i % 2 == 0]
print(nums)