#Write a program that counts for the user.
#It allows the user to enter the initial number, the final number, and the interval between successive numbers

print("Hello, welocome to Counts programme")

first = input("Enter start number:")
last = input("Enter last number:")
spacing = input("Enter spacing between this numbers:")

first = int(first)
last = int(last)
spacing = int(spacing)

if first>last and spacing>0:
    print("The starting number must not be greater than the last number.(if the distance is plus).")
else:
    print("Lets start:")
    for i in range(first, last, spacing):
        print(i, end= " ")