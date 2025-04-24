# there are many operators in python
# arithmetic operators
# comparison operators
# logical operators
# assignment operators
# identity operators
# membership operators
# bitwise operators

# the main four we will be using the most are arithmetic operators, comparison operators, logical operators, assignment operators

# so lets focus on that first then we will learn about other operators too

# arithmetic operators

a = 10
b = 5

c = a + b  # this will find the sum of two number
print(c)
c = a - b  # subtracting two numbers
print(c)
c = a * b  # multiplying 2 numbers
print(c)
c = a / b  # dividing two numbers + this will give output value in decimal
print(c)
c = a % b  # this will return remainder as the output
print(c)
c = a // b  # this will print floor value if the output is 4.5 than it will return 4 as the output
print(c)
c = a ** b  # this will return power value means 10^5 10*10*10*10*10
print(c)

# let us explore more on // and round function in python

x = 47
y = 2

z = x / y
print(z)  # the output will be 22.5
# what if i floor this
z = x // y
print(z)  # the output will be 22 even when its 22.5.

# now we'll see the round function
z = round(z)
# both floor and round are same but the difference is you can use floor directly but to use you have to call the round fuction.
print(z)


# Assignment operators
r = 1  # this is a assignment operator the value 1.4 is assigned to variable r.
r += 1
# this will  print 2.4 coz we have added 1 to r. r = r + 1 in short (r += 1).
print(r)
r -= 1
r *= 1
r /= 1

if r < 7:
    print(r)
    r %= 1
