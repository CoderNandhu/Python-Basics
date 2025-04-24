nums = [1, 2, 3, 4, 5, 6] # list of numbers


# function sum of odd numbers
def sum_of_odds(nums):
    sum = 0
    for num in nums:
        if  num % 2 != 0:
            sum = sum + num
    return sum

sum = sum_of_odds(nums)
print(sum)
