#Danny Radosevich
#COSC1101

import json 

with open("example.json","w") as json_file:
    numbers = [4,8,15,16,23,42]
    json.dump(numbers, json_file)