# ✅ Create a dictionary where:

# Keys are "city1", "city2", "city3", etc.

# Values are the city names.

cities = ["Paris", "New York", "Tokyo", "London", "Sydney"]

city = {} # empty dictionary

for i, value in enumerate(cities):
    key = "city" + str(i+1)
    print(key) # to check if we are getting "city1","city2"... etc as output.
    city[key] = value

print(city)