# I have dive deeper into string immutablity and i have found how strings are stored in the memory 

# so let's try how it works

# a = "hello world!"
# b = "hello world!"

# print(a is b) # is operator is a identity operator in python

# s = "hello world!"
# t = "".join(["hello", " world!"])

# print(id(s), id(t))  # Different IDs (not interned)
# print(s is t)

import dis

def test_string_identity():
    a = "hello world!"
    b = "hello world!"
    print(a is b)

dis.dis(test_string_identity)
