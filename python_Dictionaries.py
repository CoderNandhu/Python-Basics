# Create a dictionary for your favorite movie:
# Key: "title", "year", "director"
# Fill your favorite movie details!

movie = {
    'title': "Iron Man",
    'year': 2008,
    'director' : "Jon Favreau"
}
print(movie)

# to access single values
print(movie['title'])
print(movie['director'])
print(movie['year'])

# to add values 
movie['rating'] = 5
print(movie)

# to update value
movie['rating'] = 8
print(movie)

#to delete a pair
del movie['director']
print(movie)

# now i have deleted the director key what will be the output if try to access that key
print(movie['director']) # it will throw an error

# Important dictionary methods 

print(movie.get('director'))
print(movie.keys())
print(movie.values())
print(movie.items())

person = {
    "name":"Firoz",
    "age": 22,
    "gender":"Male"
}

person.update({"age":23})
print(person)

person.pop("age")
print(person)