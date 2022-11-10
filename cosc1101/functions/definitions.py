#Danny Radosevich
#Function Definitions
#COSC1101

def greet():
    """This is a document string, this function says hi"""
    print("hi there")

greet()

def greet_name(name):
    print(f"Hello there, {name.title()}")

greet_name("class")