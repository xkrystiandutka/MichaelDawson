# Handle it
# Demonstrate exception handling

# Try/except
try:
    num = float(input("Enter number: "))
except:
    print("An error has occurred!")

# exception type specification
try:
    num = float(input("Enter number: "))
except ValueError:
    print("That was not a number!")

# handle multiple exception types
print()
for value in (None, "Hey!"):
    try:
        print("Conversion attempt:", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Some error occurred!")

print()
for value in (None, "Hey!"):
    try:
        print("Attempted conversion:", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("Only string or number conversion is possible!")
    except ValueError:
        print("Only digit string conversion is possible!")

# get exception argument
try:
    num = float(input("Enter number: "))
except ValueError as e:
    print("That wasn't a number! Or expressing it the Python way...")
    print(e)

# try/except/else
try:
    num = float(input("Enter number: "))
except ValueError:
    print("That was not a number!")
else:
    print("You entered a number", num)

input("To exit the program, press Enter.")
