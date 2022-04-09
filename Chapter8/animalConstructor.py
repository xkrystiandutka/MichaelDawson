class Critter(object):
    """Virtual Animal"""
    def __init__(self):
        print("Create new animal")
        
    def talk(self):
        print("\nHi! I'm from Critter")


crint1 = Critter()
crint2 = Critter()

crint1.talk()
crint2.talk()

input("To exit the program, press enter.")
