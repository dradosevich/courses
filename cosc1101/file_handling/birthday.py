#Danny Radosevich
#COSC1101

with open("pi_million_digits.txt") as pi_file:
    pi_mill = pi_file.read()
    pi_mill = pi_mill.replace(" ","")
    pi_mill = pi_mill.replace("\n","")

    birthday = input("enter your birthday as mmddyy ")

    if birthday in pi_mill:
        print("your birthday is in the first million digits of pi")
    else:
        print("Your birthday is not in the first million digits of pi")