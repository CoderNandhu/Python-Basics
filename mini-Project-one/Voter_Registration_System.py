# Voter Registration System

def create_profile(name, age, hobby):
    profile = {
        "name": name,
        "age": age,
        "hobby": hobby
    }
    return profile

def check_voting_eligibility(profile):
    if profile["age"] >= 18:
        print(f"{profile['name']}, you are eligible to vote!")
    else:
        print(f"{profile['name']}, you are not eligible to vote yet.")

def introduce(profile):
    print(f"Hi, I'm {profile['name']}. I'm {profile['age']} years old and I love {profile['hobby']}!")



user1 = create_profile("Nandhu", 25, "Programming")
user2 = create_profile("Arjun", 15, "Cricket")
# print(user1)

introduce(user1)
check_voting_eligibility(user1)

introduce(user2)
check_voting_eligibility(user2)
