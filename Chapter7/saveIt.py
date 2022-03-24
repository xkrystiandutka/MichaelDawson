# Save it
# Demonstrates writing data to a text file

print("Create a text file using the write() method.")
textFile = open("Chapter7/saveIt.txt", "w")
textFile.write("Line 1")
textFile.write("This is line 2")
textFile.write("This text forms line 3")
textFile.close()

print("Reading the contents of the newly created file.")
textFile = open("Chapter7/saveIt.txt", "r")
print(textFile.read())
textFile.close()

print("Creating a text file using the writelines() method.")
textFile = open("Chapter7/saveIt.txt", "w")
lines = ["Line 1\n",
         "This is line 2\n",
         "This text forms line 3"]
textFile.writelines(lines)
textFile.close()

print("Reading the contents of the newly created file.")
textFile = open("Chapter7/saveIt.txt", "r")
print(textFile.read())
textFile.close()

input("To exit the program, press enter.")

