# What number is it?
#
# The computer randomly picks a number between 1 and 100
# The player tries to guess it and the computer tells him
# if the number is too big, too small,
# Correct.

print("Welcome to the game 'Guess number'!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few tries as possible")

import random

the_number = random.randint(1, 100)
guess = int(input("This number is "))
tries = 1

while guess != the_number:
    if guess > the_number:
        print("Too much...")
    else:
        print("Too low...")
            
    guess = int(input("This number is "))
    tries += 1


print("You guessed it! That number is", the_number)
print("To succeed you only needed", tries, "tries!")
  
input("To exit the program, press enter.")


