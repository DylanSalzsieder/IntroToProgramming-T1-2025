item = 0
tranq = 0
diddy = "your neighbor"
diddy_sleeping = 0
def fail():
    print("You jumped in a gutter because you didn't enter one of the numbers listed")
    print("Would you like to start from the beginning?")
    choice = input("1. Yes\n2. No\n>")
    if choice == 1:
        inside_house()


def encounter_end():
    print("-" * 100)


def StartA():
    print("Do you want to start an adventure?")
    choice = input("1. Yes\n2. No\n>")
    if choice == "1":
        encounter_end()
        inside_house()
    elif choice == "2":
        print("You stay at home and live out your life drinking grimace shakes and eating mangoes with mustard")
    else:
        fail()


def inside_house():
    global item
    print("You walk into the kitchen")
    print("Do you want to take the 6 dollars on the counter or the 7 mangoes in the fridge?")
    choice = input("1. 6 Dollars\n2. 7 Mangoes\n>")
    if choice == "1":
        item = "6 dollars"
        print("You take your roommate's money and leave the house")
        encounter_end()
        leave_house()
    elif choice == "2":
        item = "7 mangoes"
        print("You take your roommates mangoes and leave the house")
        encounter_end()
        leave_house()
    else:
        fail()


def leave_house():
    print("You approach the end of your driveway and stand next to your mailbox")
    print("Do you walk down the street or go to the neighbor's house?")
    choice = input("1. Walk down the street\n2. Go to the neigbor's house\n>")
    if choice == "1":
        print("You walk down the street")
        encounter_end()
        down_street()
    elif choice == "2":
        print("You walk to the neighbor's house")
        encounter_end()
        print("You arrive and walk up your neighbor's driveway and the garage is open")
        neighbor_house()
    else:
        fail()


def down_street():
    print("As you walk down the street, you see some dogs and follow them")


def neighbor_house():
    print("What do you want to do?")
    choice = input("1. Knock on the front door\n2. Enter the house through the garage\n3. Walk down the street\n>")
    if choice == "1":
        print("You knock on your neigbor's door")
        encounter_end()
        neighbor_door()
    elif choice == "2":
        print("You walk past the tesla cybertruck and inside the house through the open door leading to the garage")
        encounter_end()
        neighbor_basement()
    elif choice == "3":
        print("You walk down the street")
        encounter_end()
        down_street()
    else:
        fail()


def neighbor_door():
    global diddy
    print("Your neigbor arrives at the door")
    print("You recognize him from tv as Diddy")
    diddy = "Diddy"
    print("Diddy tells you that he's having a party and asks you to join him")
    print("What do you say?")
    choice = input("1. Yes\n2. No\n>")
    if choice == "1":
        print("Diddy walks you into his basement")
        print("You see Diddy's victims tied to a chair and he traps you in his basement forever")
    if choice == "2":
        print("Diddy is disapointed and shuts the door")
        encounter_end()
        neighbor_house()
    else:
        fail()


def neighbor_basement():
        global tranq
        print("You walk down the steps into" + diddy + "'s basement")
        print("As you open the door many people look at you and run out the door")
        print("In the basement there is a lock on the door")
        print("Do you use your " item + " on the door?")
        choice = input("1. Yes\n2. No\n>")
        if choice == "1":
            if item == "6 dollars":
                print("The door accepts the money and opens")
                print("Inside the door there is a tranquilizer gun and you take it")
                tranq = 1
                end_encounter()
                diddy_sleep()
            else:
                print("You don't have the right item and " + diddy + " locks you in his basement forever")
        elif choice == "2":
            print("You walk back outside")
            encounter_end()
            neighbor_house()
        else:
            fail()


def diddy_sleep():
    global diddy_sleeping
    print("Diddy then starts walking downstairs and sees you")
    print("You fire the tranquilizer and Diddy falls to the ground twitching")
    choice = input("Do you tie up Diddy as he's twitching up or run upstairs?")
    if choice == "1":
        print("Diddy wakes up trying to resist but he's too weak and you manage to tie him up to a chair")
        print("You defeated Diddy and are considered a hero, all of his victims that saw the whole thing praise you and you live happily ever after")
    elif choice == "2":
        diddy_sleeping = 1
        print("You go upstairs and Diddy's victims are all trapped so you open the front door with the 6 dollars")
        print("They all thank you and run outside")
        encounter_end()
        print("You walk down the street")
        down_street()
    else:
        fail()


StartA()
