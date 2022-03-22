#Improve the function ask_number() so that the function can be called with a step value. Make the default value of step 1

def askNumber(question, low, high, step = 1):
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response

askNumber("Choose a number 0-50 that is divisible by 5", 0, 50, 5)