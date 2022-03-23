# Read it
# Demonstrates reading data from a text file

print("Open and close a file.")
textFile = open("Chapter7/readIt.txt", "r")
textFile.close()

print("Reading characters from a file.")
textFile = open("Chapter7/readIt.txt", "r")
print(textFile.read(1))
print(textFile.read(7))
textFile.close()

print("Read entire file in one go.")
textFile = open("Chapter7/readIt.txt", "r")
whole_thing = textFile.read()
print(whole_thing)
textFile.close()

print("Reading characters from a line.")
textFile = open("Chapter7/readIt.txt", "r")
print(textFile.readline(1))
print(textFile.readline(7))
textFile.close()

print("Read one line at a time.")
textFile = open("Chapter7/readIt.txt", "r")
print(textFile.readline())
print(textFile.readline())
print(textFile.readline())
textFile.close()

print("Read entire file into list.")
textFile = open("Chapter7/readIt.txt", "r")
lines = textFile.readlines()
print(lines) 
print(len(lines))
for line in lines:
    print(line)
textFile.close()

print("Fetch file contents line by line using loop.")
textFile = open("Chapter7/readIt.txt", "r")
for line in textFile:
    print(line)
textFile.close()

input("To exit the program, press the Enter key.")