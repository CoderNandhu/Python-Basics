nums = []

for i in range(10):
    if i % 2 == 0:
        nums.append(i)
    else:
        nums.append("odd")
print(nums)

nums = [i if i % 2 == 0 else "odd" for i in range(10)]
print(nums)