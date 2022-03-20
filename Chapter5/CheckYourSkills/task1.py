# Create a program that prints out a list of words in a random order
# The program should output all the words without any repetitions.
#https://stackabuse.com/python-get-number-of-elements-in-a-list/
from itertools import count
import random

words = ["python", 'programming', 'computer', 'mouse', 'keyboard', 'test', 'test2']
numberOfElements = len(words)

print(random.sample(words, numberOfElements))
