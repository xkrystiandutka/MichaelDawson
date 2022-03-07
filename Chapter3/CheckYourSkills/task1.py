# Write a program that simulates a fortune cookie.
# The program should display one of five unique predictions, making a random selection each time it is run.

print("Drawing of lots")

import random

fate = random.randint(1, 5)

if fate == 1:
    print("You will be rich")
elif fate == 2:
    print("Your car will break down")
elif fate == 3:
    print("You will receive an inheritance")
elif fate == 4:
    print("You will live to be 100")
elif fate == 5:
    print("You will become bankrupt")

input("To exit the program, press enter.")