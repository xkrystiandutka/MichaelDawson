# Best results
# Demonstrates list methods

scores = []

choice = None
while choice != "0":

    print(
    """
    Best scores
    
    0 - finish
    1 - show results
    2 - add result
    3 - remove result 
    4 - sort the results
    """
    )
    
    choice = input("You choose: ")
    print()

    # end program
    if choice == "0":
        print("Goodbye.")

    # print table of best results
    elif choice == "1":
         print("Top scores")
         for score in scores:
            print(score)

    # add the score
    elif choice == "2":
        score = int(input("What score did you get?: "))
        scores.append(score)

    # remove the score
    elif choice == "3":
        score = int(input("Which score did you remove?: "))
        if score in scores:
            scores.remove(score)
        else:
            print(score, "not in score list.")

    # sort the scores
    elif choice == "4":
        scores.sort(reverse=True)

    # unknown option
    else:
        print("Unfortunately,", choice, "is not a valid choice.")
  
input("To exit the program, press enter.")
