# Scenario:

# The college has two sports teams:

football_team = {"Alice", "Bob", "Charlie", "Diana"}

basketball_team = {"Charlie", "Eve", "Frank", "Alice"}

# Tasks to complete:

# Find students who play both football and basketball.
print(f"Players who played football and basketball are: {football_team.intersection(basketball_team)}")

# Find students who play only football.
print(f"Players who played football are: {football_team.difference(basketball_team)}")


# Find students who play only basketball.
print(f"Players who played basketball are: {basketball_team.difference(football_team)}")

# Find students who are in either football or basketball (or both).
football_basketball = football_team.symmetric_difference(basketball_team)
print(f"the player in either football or basketball or in both are: {football_basketball}")
# Check if the football team and basketball team have completely different members.
different = football_team.isdisjoint(basketball_team)
print(f"checking the footbll team and basketball team have different members:{different}")
