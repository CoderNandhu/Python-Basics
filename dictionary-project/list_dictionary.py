# Practice 1: Student Subjects
# Create a dictionary student.
student = {
    "name" : "Firoz",
    "age": 22,
    "subjects": ["Math", "Science", "English"]
}
# Keys: "name", "age", "subjects".

# "subjects" should be a list like ["Math", "Science", "English"].

# Print the student's name.
print(student.get("name"))

# Print all subjects one by one.
for subject in student["subjects"]:
    print(subject)



# Practice 2: Movie Actors
# Create a dictionary movie.
movie = {
    "title": "The Avengers",
    "year": 2011,
    "actors":["robert", "chris", "mark"]
}
# Keys: "title", "year", "actors".

# "actors" should be a list like ["Actor1", "Actor2", "Actor3"].

# Print movie title.
print(movie.get("title"))

# Print all actors.
print(movie.get('actors'))
for actor in movie["actors"]:
    print(actor)