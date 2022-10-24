#Danny Radosevich
#COSC1101

import json 

with open("example.json") as json_file:
    numbers = json.load(json_file)
    print(numbers)