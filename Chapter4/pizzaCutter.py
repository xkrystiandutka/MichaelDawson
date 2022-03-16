# pizza cutter

word = "pizza"

print(
"""
  A 'workbook' for creating snippets

      0   1   2   3   4   5
      +---+---+---+---+---+ 
      | p | i | z | z | a | 
      +---+---+---+---+---+ 
     -5  -4  -3  -2  -1

"""
)

print("Enter the starting and ending index of the string slice 'pizza'.")
print("To complete the slice creation, in response to the prompt 'Begin:'\n"
      + "press enter.")

start = None
while start != "":
    start = (input("Start: "))
    
    if start:
        start = int(start)

        finish = int(input("End: "))

        print("word[", start, ":", finish, "] to", end=" ")
        print(word[start:finish])
  
input("To finish the program, press enter.")