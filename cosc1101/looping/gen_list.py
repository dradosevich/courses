# Danny Radosevich
#Generate a list

towns = open("wyoming_towns.txt","r").read()
towns = towns.split("\n")

for town in towns:
    town = town.split("\t")[1]
    """
    if "," in town:
        t_towns = town.split(",")
        for t in t_towns:
            if "and" in t:
                t = t.replace(",","")
                twn = t.split("and")

                for tw in twn:
                    print(f'"{tw.rstrip()}",')
            print(f'"{t.rstrip()}",')
    elif "and" in town:
        twn = town.split("and")
        for t in twn:
            print(f'"{t.rstrip()}",')"""
    print(f'"{town.rstrip()}",')