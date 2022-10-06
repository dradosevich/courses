#Danny Radosevich
#if statements
#COSC1101

#simple ifs
age = int(input("Please enter your age: "))
if(age < 21):
    print("No going to the bars for you!")
if(age >=21):
    print("Still avoid the buck")

#if-else
age = int(input("Please input your age: "))
if age < 17:
    print("No R rated movies for you")
else:
    print("You can see the movie!")

#if-elif-else
age = int(input("please enter your age: "))
if age <=4:
    print("dinner is free")
elif (age >= 4) and (age < 18):
    print("dinner is $7.00")
else:
    print("dinner is $10.00")

#multiple elifs
if age <=4:
    print("dinner is free")
elif  (age < 18):
    print("dinner is $7.00")
elif age == 18:
    print("dinner is $9.00")
else:
    print("dinner is $10.00")


age = 4
if age < 6:
    print(f"{age} < 6")
if age > 0:
    print(f"{age} > 0")
    
