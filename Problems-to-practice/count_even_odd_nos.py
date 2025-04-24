
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# first i have to check for the odd numbers in the list

def count_odd(nums):
    count = []
    for num in nums:
        if num % 2 != 0:
            count.append(num)
    return count

# count_odd(nums)
count_of_odd = count_odd(nums)
print(len(count_of_odd))


def count_even(nums):
    count = []
    for num in nums:
        if num % 2 == 0:
            count.append(num)
    return count
    
count_of_even = count_even(nums)
print(len(count_of_even))
