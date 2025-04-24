# Prints all the numbers.

# Prints how many numbers are even and how many are odd.

# Prints the sum of all even numbers.

# Prints the sum of all odd numbers.

# Prints the biggest number and the smallest number.

numbers = [12, 5, 8, 3, 17, 24, 6, 9]
even_number = []
odd_number = []

for num in numbers:
    if num % 2 == 0:
        even_number.append(num)
    else:
        odd_number.append(num)

print(even_number)
print(odd_number)

sum_of_even = sum(even_number)


sum_of_odd = sum(odd_number)


avg_of_even = sum_of_even / len(even_number)


avg_of_odd = sum_of_odd / len(odd_number)

greater_number_in_even = max(even_number)
greater_number_in_odd = max(odd_number)
smaller_number_in_even = min(even_number)
smaller_number_in_odd = min(odd_number)


print(f"Sum, Average, Greater and Smaller of even number in the list are : Sum = {sum_of_even} , Average = {avg_of_even}, Greater = {greater_number_in_even}, Smaller = {smaller_number_in_even}")
print(f"Sum and Average, Greater and Smaller of odd number in the list are : Sum = {sum_of_odd} , Average = {avg_of_odd}, Greater = {greater_number_in_odd}, Smaller = {smaller_number_in_odd} ")