# Best results 2.0
# Demonstrates nested sequences

scores = []

choice = None
while choice != "0":

    print(
    """
    Top scores 2.0
    
    0 - finish
    1 - display result
    2 - add result
    """
    )
    
    choice = input("You choose: ")
    print()

    # end
    if choice == "0":
        print("Goodbye.")

    # display the table of best results
    elif choice == "1":
        print("Top scores")
        print("GRADER")
        for entry in scores:
            score, name = entry    
            print(name, "■", score)

    # add a score
    elif choice == "2":
        name = input("Enter player name: ")
        score = int(input("What score did the player get?: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5] # keep only the top 5 scores

    # unknown option
    else:
        print("Unfortunately,", choice, "is not a valid choice.")
  
input("To exit the program, press enter.")
