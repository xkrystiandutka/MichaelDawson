# Message analyser

message = input("Enter message: ")

print("The length of your message is:", len(message))

print("\nMost commonly used letter in Polish, 'a',")
if 'a' in message:
    print("occurred in your message.")
else:
    print("did not occur in your message.")

input("To exit the program, press the Enter key.")