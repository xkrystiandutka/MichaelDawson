# Write a character creator program for a role-playing game. The player should be given a pool of 30 points to spend on four attributes: strength, health, wisdom, and dexterity. 
# The player should be able to spend points from the pool on any attribute and should also be able to take points from an attribute and put them back into the pool.

print ("create a character! you have points to assign to strength, health, wisdom, and dexterity.")
name = input("what's your character's name? ")
points=30
attributes=("health", "strength", "wisdom", "dexterity")
strength=0
health=0
wisdom=0
dexterity=0

while True:
    print ()
    print ("you have", points, "points left.")
    print (
    """
    1-add points
    2-take points
    3-see points per attribute
    4-exit
    """ )
    choice=input("choice: ")
    if choice=="1":
        attribute=input("which attribute? strength, health, wisdom, or dexterity? ")
        if attribute in attributes:
            add=int(input("how many points? "))
            if add<=points and add>0:
                if attribute=="strength":
                    strength+=add
                    print (name, "now has", strength, "strength points.")
                elif attribute=="health":
                    health+=add
                    print (name, "now has", health, "health points.")
                elif attribute=="wisdom":
                    wisdom+=add
                    print (name, "now has", wisdom, "wisdom points.")
                elif attribute=="dexterity":
                    dexterity+=add
                    print (name, "now has", dexterity, "dexterity points.")
                points-=add
            else:
                print ("invalid number of points.")
        else:
            print ("invalid attribute.")
    elif choice=="2":
        attribute=input("which attribute? strength, health, wisdom, or dexterity? ")
        if attribute in attributes:
            take=int(input("how many points? "))
            if attribute=="strength" and take<=strength and take>0:
                strength-=take
                print (name, "now has", strength, "strength points.")
                points+=take
            elif attribute=="health" and take<=health and take>0:
                health-=take
                print (name, "now has", health, "health points.")
                points+=take
            elif attribute=="wisdom" and take<=wisdom and take>0:
                wisdom-=take
                print (name, "now has", wisdom, "wisdom points.")
                points+=take
            elif attribute=="dexterity" and take<=dexterity and take>0:
                dexterity-=take
                print (name, "now has", dexterity, "dexterity points.")
                points+=take
            else:
                print ("invalid number of points.")
        else:
            print ("invalid attribute.")
    elif choice=="3":
        print ("strength -", strength)
        print ("health -", health)
        print ("wisdom -", wisdom)
        print ("dexterity -", dexterity)
    elif choice=="4":
        if points==0:
            break
        else:
            print ("use all your points!")
    else:
        print ("invalid choice.")
print ("congrats! you're done designing "+name+'.')
print (name, "has", strength, "strength points,", health, "health points,", wisdom, "wisdom points, and", dexterity, "dexterity points.")