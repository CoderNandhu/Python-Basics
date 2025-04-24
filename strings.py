# let us learn about string and it's methods

# caasting

from turtle import title


year = str(1980)
statement = "I love rock music of "+ year+"'s."
print(type(year))
print(statement)
# this is called casting year variable hols the value as integer but using constructor function we converted it into string.
# there are some rules in casting for ex:

#a = "21" # string value
a = int("21") # after casting string value to integer
b = 51 # integer value

print(type(a))
print(type(b))

# we can not add this operation as it will give an error coz one value is in string and another value is of integer
# now we have to cast it into integer to perform the calculation

print( a + b)

print("")

# build a menu 

title = "menu".upper()
print(title.center(20,"-"))
print("Coffee".ljust(16,".")+ " $1")
print("Muffin".ljust(16,".")+ " $2")
print("Cheesecake".ljust(16,".")+ " $4")
print("ColdCoffee".ljust(16,".")+ " $3")

# in this build menu we have use some of the string methods 
# upeer()
# ljust()
# center()
# there are many more string methods we can check it on w3school or python documentation.
