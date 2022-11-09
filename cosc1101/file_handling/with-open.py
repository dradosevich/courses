#Danny Radosevich
#COSC1101
#with file opening

with open("pi.txt") as pi_file:
    pi_contents = pi_file.read()
print(pi_contents)

pf = open("pi.txt")
pc = pf.read()
print(pc)
pf.close()