# Birthday wishes
# Demonstrates named arguments and default parameter values

# positional parameters
def birthday1(name, age):
    print("Happy birthday,", name, "!", "You already have", age, "lat.\n")

# parameters with default values
def birthday2(name = "Krystian", age = 5):
    print("Happy birthday,", name, "!", " You already have", age, "lat.\n")


birthday1("Krystian", 5)
birthday1(5, "Krystian")
birthday1(name = "Krystian", age = 5)
birthday1(age = 5, name = "Krystian")

birthday2()
birthday2(name = "Catherine")
birthday2(age = 12)
birthday2(name = "Catherine", age = 12)
birthday2("Catherine", 12)

input("To exit the program, press enter.")
