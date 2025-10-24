item = 0
diddy = "your neighbor"
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
        neighbor_house()
    else:
        fail()


def down_street():
    print()


def neighbor_house():
    print("You arrive and walk up your neighbor's driveway and the garage is open")
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



def neighbor_basement():
        print("You walk down the steps into" + diddy + "'s basement")


StartA()