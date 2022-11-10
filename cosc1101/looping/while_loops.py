# Danny Radosevich
# While loops
# COSC1101

import random 

#just over a number range
i = 0 
while i < 3:
    print(i)
    i += 1

#with an else 
i = 0
while i < 73672:
    i += 1
else:
    print(i)

# using a control varaible 
control_var = True 
i = 0
while control_var:
    i += 1
    if random.randint(0,20) == 13:
        print(13)
        control_var = False
print(f"The while loop ran {i} times")

#control statements 
#continue
print("continue")
wyo = "Wyoming"
for c in wyo:
    if c == "W" or c == "m":
        continue
    print(c)

#break
print("break") 
for c in wyo:
    if c == "m":
        break
    print(c)


for i in range(1000):
    pass

print("hi")