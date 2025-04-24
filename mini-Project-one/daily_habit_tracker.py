
def create_habit(name):
    habit = {
        "name": name,
        "completed": False  
    }
    return habit

habit_list = [
    create_habit("reading"),
    create_habit("exercise"),
    create_habit("meditation"),
    create_habit("coding")
]


def mark_complete(habit):
    if habit["completed"] == False:
        habit["completed"] = True
        print(f"Habit '{habit['name']}' is now marked as completed!")
    else:
        print(f"Habit '{habit['name']}' was already completed!")

for habit in habit_list:
    print(f"Habit: {habit['name']}, Completed: {habit['completed']}")

def display_habits():
    for habit in habit_list:
        if habit["completed"]:
            status = "✔️"
        else:
            status = "❌"  
        print(f"Habit: {habit['name']} {status}")  # ✅ Moved inside the loop


mark_complete(habit_list[0])
display_habits()
