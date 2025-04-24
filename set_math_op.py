# union()
set1 = {1, 2, 3, 5, 6}
set2 = {0, 1, 2, 4, 7, 8, 9} 

union_set = set1.union(set2)
print(union_set)

a = {10, 20, 30}
b = {30, 40, 50}

c = a.union(b)
print(c) # the output will be {50, 20, 40, 10, 30} as there is no order for set
# intersection()
x = {100, 200, 300}
y = {300, 400, 500}

common = x.intersection(y)
print(common) # the output will be {300} as it checks for the common value in x and y
# difference()

p = {10, 20, 30, 40}
q = {30, 40, 50, 60}

# before print i went through the code and the expected output is {10, 20}
r = p.difference(q)
print(r)# it will check for the difference in the first set and as per my assumption the output will be {10,20}


# Practice 1
p = {10, 20, 30}
q = {30, 40, 50}
print(p.symmetric_difference(q))  # What will be the output?
# the output will be {10,20,40,50} it doesn't print the common value exists in the sets.

# Practice 2
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))  # True or False?
# True

# Practice 3
x = {100, 200, 300, 400}
y = {100, 200}
print(x.issuperset(y))  # True or False?
# true 

# Practice 4
set1 = {5, 10, 15}
set2 = {20, 25, 30}
print(set1.isdisjoint(set2))  # True or False?
# true

# Practice 5
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.difference(set_b))  # What's the output?
# the output will be {1,2}
