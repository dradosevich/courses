#Danny Radosevich
#A example for Monty Hall 3 door paradox

import random 

times_played = 0
times_won = 0
times_lost = 0
times_switched = 0
times_stayed = 0
times_switched_and_won = 0 
times_switched_and_lost = 0
times_stayed_and_won = 0
times_stayed_and_lost = 0


print("Welcome to the Monty Hall simulator.")
print("This will demonstrate that when given the choice to switch you should")
print("The math works out to your first guess is 1/3 chances of being correct")
print("When given the choice to chance the host -Monty- will eliminate a prizeless door")
print("With the two doors left they together have a 2/3 chance of winning")
print("Try it out!, if you want to stop simply type \"exit\"")

keep_going = True
while keep_going:
    doors = ["1","2","3"]
    random.seed()
    secret_door = random.choice(doors)
    #doors.remove(secret_door)
    door_selected = False
    your_door = ""
    while not door_selected:
        door = input("Please select a door by entering 1 or 2 or 3\n")
        if door == "1" or door == "2" or door == "3":
            your_door = door
            doors.remove(your_door)
            door_selected = True
            print("You slected door %s" %(your_door))
        elif door == "exit":
            break
        else:
            print("Door not properly selected")
                
    if door_selected:
        print("-")
        monty_opening = True
        while monty_opening:
            door_monty_opened = random.choice(doors)
            if door_monty_opened != secret_door:
                print(door_monty_opened)
                print(doors)
                doors.remove(door_monty_opened)
                monty_opening = False
        #doors.remove(door_monty_opened)
        last_door = doors[0]
        print("Monty opened door %s "%(door_monty_opened))
        print("You initially chose door %s door %s also remains" %(your_door,last_door))
        switch_selected = False
        while not switch_selected:
            switch = input("would you like to switch doors: y/n\n")
            if switch == "y" or switch == "n":
                switch_selected = True
                if switch == "y":
                    print("You chose to switch your door from %s to %s"%(your_door,last_door))
                    print("Your new door is %s"%last_door)
                    times_switched += 1
                    if last_door == secret_door:
                        times_played += 1
                        times_won += 1
                        times_switched_and_won += 1
                        print("congrats! your switch paid off, you won!")
                    else:
                        times_played += 1
                        times_switched_and_lost += 1
                        times_lost +=1 
                        print("Unfortunately the switch failed you")
                if switch == "n":
                    times_stayed +=1
                    print("you are staying with door %s"%(your_door))
                    if your_door == secret_door:
                        times_played += 1
                        times_won += 1
                        times_stayed_and_won +=1
                        print("Congrats, your door was the secret door")
                    else:
                        times_played += 1
                        times_lost += 1
                        times_stayed_and_lost += 1
                        print("Dang, should have switched")
            else:
                print("Invalid answer")
    print("Post match recap:\ntimes play: %s\ntimes_won: %s\n times_lost: %s\ntimes switched: %s\n times stayed %s"%(times_played,times_won,times_lost,times_switched,times_stayed))
    print("Switch and won has happened %s/%s" %(times_switched_and_won,times_played))
    print("Stayed and lost has happened %s/%s" %(times_stayed_and_lost,times_played))
    print(" the switch would have won %d/%s times" %((int(times_switched_and_won)+int(times_stayed_and_lost)),times_played))
        
