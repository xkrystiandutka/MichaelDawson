# Hero inventory
# Demonstrate the creation of tuples

# Create an empty tuple
inventory = ()

# Treat the tuple as a condition
if not inventory:
    print("You have empty hands.")

input("To continue your mission, press enter.")

# create a tuple containing some elements
inventory = ("sword",
             "armor",
             "shield",
             "healing drink")

# display the tuple
print("List contents of tuple:")
print(inventory)

# display each item of the tuple
print("Items of your inventory:")
for item in inventory:
    print(item)

input("To exit the program, press enter.")