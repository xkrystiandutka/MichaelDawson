# Dice Roll

import random

die1 = random.randint(1,6)
die2 = random.randrange(6) + 1

total = die1 + die2

print ("You have thrown away the result", die1)
print ("You have thrown away the result", die2)
print("Your score is equal", total)

input("\n\nTo end the programme, press the Enter key.")
