# Losing the battle
# Demonstrates the dreaded infinite loop

print("Your lone hero is surrounded by a vast army of trolls.")
print("A great mass of their rotten green bodies stretches to the horizon.")
print("The hero draws his sword from its sheath, ready to fight his final battle.")

health = 10
trolls = 0
damage = 3

while health > 0:
    trolls += 1
    health -= damage

    print("Hero defeats evil troll, " \
          "but takes damage and loses", damage, "health points")

print("Your hero fought bravely and defeated", trolls, "trolls.")
print("But unfortunately your hero is already dead.")

input("To exit the program, press enter.")
