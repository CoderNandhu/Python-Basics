def can_vote(name, age):
    if age >= 18:
        print(f"{name}, you are eligible to vote!")
    else:
        print(f"{name}, you are not eligible to vote yet.")
    pass

can_vote("Nandhu", 25)
can_vote("Arjun", 16)
