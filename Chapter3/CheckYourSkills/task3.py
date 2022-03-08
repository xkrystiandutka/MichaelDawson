# What number is it?
#
# The computer randomly picks a number between 1 and 100
# The player tries to guess it and the computer tells him
# if the number is too big, too small,
# Correct. 
# Task 3 Update this program add you must aim correct answer in few tries or you lose game

print("Welcome to the game 'Guess number'!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few tries as possible")

import random

the_number = random.randint(1, 100)
guess = int(input("This number is "))
tries = 0
change = 5
msg = print("\tToo much tries. You lost. Better Luck Next time!That number is", the_number)

while guess != the_number and change > 0:

    guess = int(input("Enter the guessed number: "))

    if guess > the_number:
        print("Too much...")
        tries += 1
        change -= 1
        print(tries)
    elif guess < the_number:
        print("Too low...")
        tries += 1
        change -= 1
        print(tries)
    elif guess == the_number:
        print("You guessed it! That number is", the_number)
        print("To succeed you only needed", tries, "tries!")
    continue
print(msg)
  
input("To exit the program, press enter.")
