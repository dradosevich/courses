#Danny Radosevich
#COSC1101
#going line by line in a file

filename = "pi.txt"

with open(filename) as pi_file:
    #by splitting the string into lines manually
    pi_string = pi_file.read()
    pi_lines = pi_string.split("\n")
    print(type(pi_lines))
    for line in pi_lines:
        print(line)

with open(filename) as pi_file:
    #by reading lines 
    pi_read_lines = pi_file.readlines()
    print(type(pi_read_lines))
    for line in pi_read_lines:
        print(line.rstrip())


with open(filename) as pi_file:
    print(type(pi_file))
    for line in pi_file:
        print(line.rstrip())