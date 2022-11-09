# Danny Radosevich
# COSC1101
# Classes

class Dog: #1
    """A simple dog class""" #2
    def __init__(self,name, age, breed): #3
        """Initialize the attributes""" 
        self.name = name  #4
        self.age = age 
        self.breed = breed 

    def sit(self): #5
        print(f"{self.name} is sitting")
    def shake(self):
        print(f"{self.name} is offering their paw to you")

#Create an instance of dog, for Apollo
apollo = Dog("Apollo",2,"GSD/Husky")

#print out the attributes of Apollo
print(f"My dog's name is {apollo.name}, he is a {apollo.breed} "+
f"and he is {apollo.age} yeas old.")

#Call the methods
apollo.sit()
apollo.shake()

#create another dog 
rex = Dog("Rex",5,"Lab")
print(f"My dog's name is {rex.name}, he is a {rex.breed} "+
f"and he is {rex.age} yeas old.")
