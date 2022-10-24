#Danny Radosevich
#COSC1101
#Working with file contents


filename = "pi.txt"
pi_string = ""
with open(filename) as pi_file:
    #by going through the file object
    for line in pi_file:
        pi_string += line.lstrip().rstrip() 
print(pi_string)