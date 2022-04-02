# Knowledge tournament
# A game to test general knowledge, reading data from a plain text file

import sys

def open_file(file_name, mode):
    """Open file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open file", file_name, "Program will be terminated.", e)
        input("To exit the program, press enter.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return the next line of the quiz file after formatting it."""
    line = the_file.readline()
    line = line.replace("/", "ƒ")
    return line

def next_block(the_file):
    """Return the next block of data from the quiz file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        
    explanation = next_line(the_file) 

    return category, question, answers, correct, explanation

def welcome(title):
    """Welcome a player and retrieve their name."""
    print("Welcome to the knowledge tournament!")
    print("\n", title, "\n")
 
def main():
    trivia_file = open_file("Chapter7/quiz.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get the first block
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        # ask question
        print(category)
        print(question)
        for i in range(4):
            print("■", i + 1, "-", answers[i])

        # get an answer
        answer = input("What is your answer?: ")

        # check answer
        if answer == correct:
            print("_Correct answer!", end=" ")
            score += 1
        else:
            print("incorrect answer.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # get another block
        category, question, answers, correct, explanation = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("Your final score is", score)
 
main()  
input("To exit the program, press enter.")
