#Write a program that tosses a coin 100 times and then gives the result of eagles and tail

import random

print('\nPrepare for the draw of 100 coins!!! ')


eagles = 0
tail = 0
tries = 0

while tries < 100:
    coin = random.randint(1,2)
    if coin == 1:
        eagles += 1
    else:
        tail += 1
    tries += 1

print("Drawing results:")
print("Eagles - ", eagles)
print("Tail - ", tail)
print(tries)

input("To exit the program, press enter.")
