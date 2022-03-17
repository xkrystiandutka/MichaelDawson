# Mixed up the letters
# Shuffled letters
# The computer chooses a word at random and then mixes up the letters
# The player should guess the original word

import random

# Create a sequence of words to choose from
WORDS = ("python", "machine learning", "artificial intelligence", "algorithm")
# randomly select one word from the sequence
word = random.choice(WORDS)
# create a variable to use later to check if the answer is correct
correct = word

# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Welcome to the game 'Jumbled letters'!
        
   Put the letters in order to recreate the correct word.
(To complete the guess, press the enter key without entering an answer.)
"""
)
print("Guess what the word is:", jumble)

guess = input("Your answer: ")
while guess != correct and guess != "":
    print("Unfortunately, that's not the word.")
    guess = input("Your answer: ")
    
if guess == correct:
    print("Correct ! You guessed !")

print("Thank you for playing.")

input("To exit the program, press enter.")
