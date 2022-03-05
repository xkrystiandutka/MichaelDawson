#Write a tip calculator program that should calculate a 15% tip on the bill and a 20% tip on the restaurant bill.

bill = input("How much did you pay at the restuarant? ")
bill = int(bill)

tip15 = bill * 0.15
tip20 = bill * 0.2

print("If you want to pay 15% tip you should leave: ", tip15)
print("If you want to pay 20% tip you should leave: ", tip20)