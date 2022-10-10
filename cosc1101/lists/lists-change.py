#Danny Radosevich
#COSC1101
#Lists changing

#changing elements
names = ["Pistol Pete","Cowboy Joe","Pokes"]
print(names)
names[2] = "Cowboys"
print(names)

#appending elements 
names.append("Pokes")
print(names)

#building a list
towns = [] 
towns.append("Laramie")
towns.append("Jackson Hole")
towns.append("Cheyenne")
towns.append("Sheridan")
print(towns)

#inserting to a list
towns.insert(2,"Pinedale")
print(towns)

#Removing items
#the del statement
del towns[3]
print(towns)

#popping elements
town = towns.pop()
print(f"The first popped town is {town}")
print(f"The second popped town is {towns.pop()}")
print(towns)

#popping at random spots
towns.append("Cheyenne")
towns.append("Sheridan")
print(f"We are popping the element at the third index, it is {towns.pop(3)}")
print(towns)

#removing an element by value
towns.remove("Jackson Hole")
state_cap = "Cheyenne"
towns.remove(state_cap)
print(towns)