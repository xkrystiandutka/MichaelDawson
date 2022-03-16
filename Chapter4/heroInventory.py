# Hero Inventory 2.0
# Demonstrate tuples

# Create a tuple containing some items and display its contents
# using the for loop
inventory = ("sword",
             "armor",
             "shield",
             "healing drink")
print("Items in your inventory:")
for item in inventory:
    print(item)

input("To continue the game, press enter.")

# display the length of a tuple
print("Your inventory contains", len(inventory), "item(s).")

input("To continue the game, press enter.")

# check if the item belongs to the tuple, using the in operator
if "healing drink" in inventory:
    print("You will live to fight the day.")

# display one element indicated by index
index = int(input("Enter index of inventory item: "))
print("Under index", index, "is located", inventory[index])

# display the slice
start = int(input("Enter index that determines the start of the slice: "))
finish = int(input("Enter index designating the end of the slice: "))
print("inventory[", start, ":", finish, "] to", end=" ")
print(inventory[start:finish])

input("To continue the game, press enter.")

# concatenate two tuples
chest = ("gold", "gems")
print("You have found a chest that contains:")
print(chest)
print("You are adding the contents of the chest to your inventory.")
inventory += chest
print("Your current inventory is:")
print(inventory)

input("To exit the program, press enter.")
