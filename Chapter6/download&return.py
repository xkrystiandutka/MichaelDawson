from urllib import response


def display(message):
    print(message)

def giveMeFive():
    five = 5
    return five

def askYesNo(question):
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response

#main
display("That massege for you.\n")

number = giveMeFive()
print("That's the feedback for giveMeFive function:", number)

answer = askYesNo("Please input 't' or 'n':")
print("Thanks for input:", answer)

input("To exit the program, press enter.")
