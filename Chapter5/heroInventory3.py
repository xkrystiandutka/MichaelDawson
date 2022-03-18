# Hero Inventory 3.0
# Demonstrate lists

# create a list containing some items and display its contents
# using the for loop
inventory = ["sword", "armor", "shield", "healing drink"]
print("Items in your inventory:")
for item in inventory:
    print(item)

input("To continue the game, press enter.")

# display the length of the list
print("Your inventory contains", len(inventory), "item(s).")

input("To continue playing, press enter.")

# check if the item belongs to the list, using the in operator
if "healing drink" in inventory:
    print("You will live to fight the day.")

# display the one element indicated by index
index = int(input("Enter index of inventory item: "))
print("Under index", index, "is located", inventory[index])

# display the slice
start = int(input("Enter index to start slice: "))
finish = int(input("Enter index for slice end: "))
print("inventory[", start, ":", finish, "] to", end=" ")
print(inventory[start:finish])

input("To continue the game, press enter.")

# concatenate two lists
chest = ["gold", "gems"]
print("You have found a chest that contains:")
print(chest)
print("You are adding the contents of the chest to your inventory.")
inventory += chest
print("Your current inventory is:")
print(inventory)

input("To continue the game, press enter.")

# assign by index
print("You are exchanging your sword for a crossbow.")
inventory[0] = "crossbow"
print("Your current inventory is:")
print(inventory)

input("To continue the game, press enter.")

# assign by slice
print("You are using your gold and gems to buy a divination ball.")
inventory[4:6] = ["divination ball"]
print("Your current inventory is:")
print(inventory)

input("To continue the game, press enter.")

# delete item
print("In the great battle your shield is destroyed.")
del inventory[2]
print("Your current inventory is:")
print(inventory)

input("To continue the game, press enter.")

# delete the snippet
print("Tawoja's crossbow and armor were stolen by thieves.")
del inventory[:2]
print("Your current inventory is:")
print(inventory)

input("To exit the program, press enter.")