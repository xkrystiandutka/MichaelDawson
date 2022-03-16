#Without vowels

message = input("")
new_message = "Enter message: "
VOWLES = "aąeęioóuy"

print()
for letter in message:
    if letter.lower() not in VOWLES:
        new_message += letter
        print("Your message without vowels is:", new_message)

input("To exit the program, press enter.")
