# A variable that stores your age
first = "Nandhu"
last = "krishnan"


age = 25

# A variable for your full name
full_name = first +" " + last
# A list of your 3 favorite foods
fav_food =["shawarma", "biriyani", "pizza"]
# A dictionary for your profile (name, age, hobby)
profile = {
    "name": "Nandhu Krishnan",
    "age": 25,
    "hobby":"programming"
}
print(age)
print(full_name)
print(fav_food)
print(profile)
print(type(fav_food))

satement = f"Hi, I'm {profile['name']}, I'm {profile['age']} years old and I love {profile['hobby']}."

print(satement)
fav_food.append("Apples")

# print(fav_food)
# print(len(fav_food))
# print(fav_food[3])

# for x in fav_food:
#     print(x.upper())

for index, food in enumerate(fav_food):
    print(f"{index + 1}. {food.upper()}")
