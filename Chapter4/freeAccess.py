#Free access 

import random

word = "index"

print("The value of the variable is", word, "\n")

high = len(word)
low = -len(word)

for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])


input("\n\nTo exit the program, press enter")
