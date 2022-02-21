# Manipulates quotations
# Demonstrates the methods of the chain

# Quote from IBM's president, Thomas Watson, in 1943.
quote = "I think there is a world market for maybe five computers."

print("Original quote as translated:")
print(quote)

print("In capital letters:")
print(quote.upper())

print("In lowercase:")
print(quote.lower())

print("All words starting with a capital letter:")
print(quote.title())

print("With minor substitutions:")
print(quote.replace("five", "millions"))

print("The original quote remained unchanged:")
print(quote)

input("To exit the program, press enter.")

