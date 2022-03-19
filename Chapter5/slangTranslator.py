# Computer slang translator
# Demonstrates the use of dictionaries

geek = { "404": "ignorant; from the 404 error message used on the World Wide Web - page not found.",
        "Googling": "googling; searching the internet for information relating to some person.",
        "Keyboard Plaque" : "(associated with tartar)dirt accumulated on a computer keyboard.",
        "Link Rot" : "(link dieback) the process by which links to web pages become obsolete.",
        "Percussive Maintenance" : "(percussive maintenance)the repair of an electronic device by tapping.",
        "Uninstalled" : "(uninstalled) redundant; a term particularly popular during the Internet bubble period."}  

choice = None
while choice != "0":

    print(
    """
    Computer slang translator
    
    0 - end
    1 - find term
    2 - add new term
    3 - change term definition
    4 - delete term
    """
    )
    
    choice = input("You choose: ")
    print()

    # exit
    if choice == "0":
        print("Goodbye.")

    # get definition
    elif choice == "1":
        term = input("What term should I translate?: ")
        if term in geek:
            definition = geek[term]
            print("\n", term, "means", definition)
        else:
            print("\nSorry, I don't know the term", term)

    # add term-definition pair
    elif choice == "2":
        term = input("What term should I add?: ")
        if term not in geek:
            definition = input("Give a definition for this term: ")
            geek[term] = definition
            print("Term", term, "has been added.")
        else:
            print("This term already exists! Try changing its definition.")

    # change the definition of an existing term
    elif choice == "3":
        term = input("What term should I redefine?: ")
        if term in geek:
            definition = input("What is the new definition?: ")
            geek[term] = definition
            print('Term', term, "has been redefined.")
        else:
            print("This term does not exist! Try adding it.")
       
    # remove term-definition pair
    elif choice == "4":
        term = input("Which term should I delete: ")
        if term in geek:
            del geek[term]
            print("\nOK, I deleted it", term)
        else:
            print("I can't do that! The term", term, "is not in the dictionary.")
            
    # unknown option
    else:
        print("Unfortunately,", choice, "this is an invalid choice.")
  
input("To exit the program, press enter.")