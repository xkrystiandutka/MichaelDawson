# Unimportant facts

# Gets personal information from the user and then prints out true but useless information about you

name = input("Hello, what is your name? ")

age = input("How old are you? ")
age = int(age)

weight = int(input("OK, last question. How many kilograms do you weigh? "))

print("\nIf the poet ee cummings sent you an email \nhe would get back to you",
      name.lower())
print("But if he was angry, he would call you", name.upper())

called = name * 5
print("\nIf a young child tries to get your attention",)
print("Your name would take the form:")
print(called)

seconds = age * 365 * 24 * 60 * 60
print("\nYou have lived more than", seconds, "seconds.")

moon_weight = weight / 6
print("\nDid you know that on the moon your weight would be",
      moon_weight, "kg?")

sun_weight = weight * 27.1
print("On the Sun you would weigh", sun_weight, "kg (but unfortunately not for long).")

input("\n\nTo end the programme, press the Enter key.")