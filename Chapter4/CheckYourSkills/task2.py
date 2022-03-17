#Create a program that reads the message entered by the user backwards "Redrum :)"
#https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python
#Methods
#Three methods to reverse a string are explained below:
#1. Slicing

backwards = input("Write your message to be rewritten backwards:")
stringlength=len(backwards) # calculate length of the list
slicedString=backwards[stringlength::-1] # slicing 
print (slicedString) # print the reversed string

