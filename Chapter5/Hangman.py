# The gallows
#
# The classic gallows game.  The computer randomly selects a word,
# and the player tries to guess its individual letters.  If the player
# doesn't guess the whole word in time, the little guy gets hanged.

# import modules

import random


hangman = (

"""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,

"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    H""",

"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    HA""",

"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    HAN""",


"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    HANG""",


"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    HANGM""",



"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    HANGMA""",


"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    HANGMAN""")

MAX_WRONG = len(hangman) - 1
WORDS = ("ARTIFICIAL INTELLIGENCE", "MACHINE LEARNING", "API", "PROGRAMMING", "PYTHON")

# initialise variables
word = random.choice(WORDS) # word to guess
so_far = "-" * len(word) # a dash replaces a missed letter
wrong = 0 # number of wrong letters
used = [] # letters already used in guessing


print("Welcome to the game 'Gallows'. Good luck!")

while wrong < MAX_WRONG and so_far != word:
    print(hangman[wrong])
    print("You have already used the following letters: used", used)
    print("So far the puzzle word looks like this:so_far", so_far)

    guess = input("Enter letter: ")
    guess = guess.upper()
    
    while guess in used:
        print("You have already used a letter", guess)
        guess = input("Enter letter: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        

        # create a new version of the variable so_far to contain the guessed letter
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]              
        so_far = new

    else:
        
        wrong += 1

if wrong == MAX_WRONG:
    print(hangman[wrong])
    print("You've been hanged!")
else:
    print("You guessed it!")
    
print("Guess word is", word)

input("To exit the program, press enter.")