#Write a car dealer program.
#In which the user enters the price of the car and the program adds charges such as tax, registration fee, dealer preparation fee, car preparation fee.
# Calculate the tax and registration fee as a percentage of the value of the car and the other charges as a constant and display the actual price of the car.

car = input("How much cost your car? ")

car= int(car)

tax = car*0.17
tax = int(tax)
registrationFee = car*0.05
registrationFee = int(registrationFee)

commissionDealer = 1500
importTax = 2500

cost = car + tax + registrationFee + commissionDealer + importTax

print("Real price for this car is ", cost)

