# Problem:
# Imagine you are organizing a tech event.

# registered_users = {"Alice", "Bob", "Charlie", "Diana", "Eve"}

# attended_users = {"Charlie", "Eve", "Frank", "Grace"}

# Tasks:

registered_users = {"Alice", "Bob", "Charlie", "Diana", "Eve"}

attended_users = {"Charlie", "Eve", "Frank", "Grace"}

# Find out who registered but didn’t attend the event. {difference}
not_attended_users = registered_users.difference(attended_users)
print(f"User's who registered but didn't attended are {not_attended_users}")

# Find out who attended without registering. {difference}
not_registered_users = attended_users.difference(registered_users)
print(f"Users who attented without registering {not_registered_users}")

# Find users who both registered and attended.
registered_and_attended_user = registered_users.intersection(attended_users)
print(f"The user who had registered and attended are {registered_and_attended_user}")

# Check if all attendees were registered.
for i in registered_users:
    if i == attended_users:
        print(f"This attendees were registered: {i}")
# Check if there are any common users between registration and attendance.
print(f"Common users between registeration and attendance are {registered_users.intersection(attended_users)}")