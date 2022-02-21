#Trust fund participant - incorrect version
# Demonstrates a logic error

print(
"""
            Trust fund participant

Adds up your monthly expenses so that your trust fund doesn't run out
(because then you would be forced to take a real job).

Enter your required monthly expenses.  Since you are rich, ignore the
pennies and give your amounts in whole zlotys.

"""
)

car = input("Mercedes service: ")
rent = input("Downtown apartment: ")
jet = input("Renting a private plane: ")
gifts = input("Gifts: ")
food = input('Dining at restaurants: ')
staff = input("Staff (domestic servants, cook, driver, assistant): ")
guru = input("Personal guru and coach: ")
games = input("Computer games: ")

total = car + rent + jet + gifts + food + staff + guru + games

print("Total:", total)

input("To exit the program, press Enter.")

# Trust fund participant - correct version
# Demonstrates type conversion
print(
"""
            Trust fund participant

Adds up your monthly expenses so that your trust fund doesn't run out
(because then you would be forced to take a real job).

Enter your required monthly expenses.  Since you are rich, ignore the
pennies and give your amounts in whole zlotys.

"""
)

car = input("Service for Mercedes: ")
car = int(car)

rent = int(input("Apartment in Downtown: "))
jet = int(input("Rent a private plane: "))
gifts = int(input("Gifts: "))
food = int(input('Dining at restaurants: '))
staff = int(input("Staff (domestic servants, cook, driver, assistant): "))
guru = int(input("Personal guru and coach: "))
games = int(input("Computer games: "))

total = car + rent + jet + gifts + food + staff + guru + games

print("Total:", total)

input("To exit the program, press Enter.")

