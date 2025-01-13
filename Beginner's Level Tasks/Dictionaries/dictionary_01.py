#1. Create a list of your friends' names. The list should have at least 5 names.
#Create a list of tuples. Each tuple should contain a friend's name and the length of their name.
best_friends=["Ashfiya", "Zabiha", "Athufa", "Heena", "Hajira"]
tuple=[(name, len(name)) for name in best_friends]
print("The List is:", tuple)

