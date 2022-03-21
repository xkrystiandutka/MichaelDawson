# Global coverage
# Demonstrates global variables

def read_global():
    print("The value of the variable value read inside the local scope,"
          "The value of the read_global() function is:", value)

def shadow_global():
    value = -10
    print("The value of the variable value read inside the local scope,"
          "The value of the shadow_global() function is:", value)
  
def change_global():
    global value
    value = -10
    print("The value of the variable value read inside the local scope,"
          "The value of the change_global() function is:", value)

# main part of program
# value is a global variable because we are now in the global scope
value = 10
print("In the global scope, the value of the variable value has been set to:", value, "\n")

read_global()
print("After returning to the global scope, the value of the variable value is still:", value,
      "\n")

shadow_global()
print("After returning to the global scope, the value of the variable value is still:", value,
      "\n")

change_global()
print("Upon returning to the global scope, it appears that the value of the variable value",
      "\nChanged to:", value)

input("To exit the program, press enter.")