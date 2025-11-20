def start_adventure():
    print("You meet a wizard on a mountain, Do you:")
    print("1. take his quest")
    print("2. Turn back and go home")

    choice = input("> ")

    if choice == "1":
            take_quest()
    elif choice == "2":
            go_home()
    else:
        print("Invalid choice. Try again.")
        start_adventure()

def go_home():
    print("You decide it's safer at home, you have a family.THE END")

def take_quest():
    print("the wizard tells you to make your journey to slay the evil dragon, what direction do you take to the dragons layer, do you:")
    print("1.go towads the river")    
    print("2.go towards the swamp")
    choice = input("> ")

    if choice == "1":
            the_river()
    elif choice == "2":
            the_swamp()
    else:
        print("Invalid choice. Try again.")
        take_quest()

def the_river():
  print("you arive at the river with no way across what do you do:")
  print("1.wait there")
  print("2.try to swim across")
  print("3.try and walk around")
  choice = input("> ")
  if choice == "1":
            wait_there()
  elif choice == "2":
            swim_across()
  elif choice == "3":
            walk_around()
  else:
        print("Invalid choice. Try again.")
        the_river()



def swim_across():
        print("you try and swim across but realize the current is too strong and get swept away and see a waterfall in the distance do you:")
        print("1.grab onto a overhaning branch")
        print("2.dive under and hope to grab onto a rock")
        choice = input("> ")

        if choice == "1":
            grab_branch()
        elif choice == "2":
            dive_under()
        else:
         print("Invalid choice. Try again.")
        the_river()
def grab_branch():
      print("it breaks instantly as you touch it and fly off the cliff")

def dive_under():
      print("you manage to grab a rock and eventualy run out of breath and drown")

def walk_around():
      print("you try and walk around and run into some bandits, do you:")
      print("1.fight them off")
      print("2.give them everything")
      choice = input("> ")

      if choice == "1":
            fight()
      elif choice == "2":
            give()
            the_river()
      else:
        print("Invalid choice. Try again.")
        the_river()
def fight():
      print("you are out numbered and made into a slave")
      the_river()
def give():
      print("you give them all your belonging and are never seen again")



def the_swamp():
   print("you deside to test your luck in the swamp and run into the biggest snake you have ever seen do you:")
   print("1.RUN")
   print("2.fight")
   choice = input("> ")

   if choice == "1":
            run()
   elif choice == "2":
            fight_snake()
   else:
        print("Invalid choice. Try again.")
        the_river()
def run():
      print("you run as fast as you can and fall into the water and get eaten by the crocodiles")
def fight_snake():
      print("you are over powerd by the snake but some how kill the beast but loose your legs in the battle and live out your days as the SNAKE SLAYER")

def wait_there():
  print("you deside to stand and wait after a day a goblin apears do you:")
  print("1.hear him out")
  print("2.fight him")
  choice = input("> ")

  if choice == "1":
            hear_him()
  elif choice == "2":
            fight_him()
  else:
        print("Invalid choice. Try again.")
        wait_there()
def hear_him():
      print("he offers to get you across the river, and give you bit of info for your journy, for a fee do you:")
      print("1.pay fee")
      print("2.dont pay fee")
     
      choice = input("> ")

      if choice == "1":
            pay_fee()
      elif choice == "2":
            dont_pay()
      else:
        print("Invalid choice. Try again.")
        wait_there()


def fight_him():
      print("you kill him easily but cant get across the river")
      wait_there()


def pay_fee():
      print(" he sends you across the river he tells you to remember the word ,macaroon, where do you go next")
      print("1.through the dark forest")
      print("2.through the village")
      choice = input("> ")

      if choice == "1":
            dark_forest()
      elif choice == "2":
            go_villa()
      else:
        print("Invalid choice. Try again.")
        hear_him()


def dont_pay():
      print("you tell him you will not pay he begins to walk away do you:")
      print("1.force him to get you across")
      print("2.let him leave and set up camp")
      choice = input("> ")

      if choice == "1":
            force_him()
      elif choice == "2":
            set_up()
      else:
        print("Invalid choice. Try again.")
        hear_him()

def force_him():
      print(" he sends you across the river where do you go next")
      print("1.through the dark forest")
      print("2.through the village")
      choice = input("> ")

      if choice == "1":
            dark_forest()
      elif choice == "2":
            go_villa()
      else:
        print("Invalid choice. Try again.")
        hear_him()

def set_up():
      print("you fall asleep in your camp and get stung by a scorpion")
      hear_him()




def dark_forest():
      print("you enter the forest and see it has killer bats that chase you out. if only you had somthing to reatch them, see if thers somthing in the village")
      force_him()




def go_villa():
      print("you are walking through the village and are hungry but may need a bow do you:")
      print("1.buy food")
      print("2.buy a bow")
      print("3.buy a cool hat")
      choice = input("> ")
      if choice == "1":
            buy_food()
      elif choice == "2":
            buy_bow()
      elif choice == "3":
            buy_hat()
      else:
        print("Invalid choice. Try again.")
        go_villa()

def buy_food():
      print("you are no longer hungry and continue to dragon")
      contin_drag()


def buy_bow():
      print("you now have a bow with unlimited arows do you:")
      print("1.go to forest")
      print("2.continue to dragon")
      choice = input("> ")
      if choice == "1":
            contin_forest()
      elif choice == "2":
            contin_drag()  
      else:
        print("Invalid choice. Try again.")
        go_villa()

def buy_hat():
      print("every one in town compliments your hat and you contine on your quest")
      contin_drag()

def contin_forest():
      print("you go to the forest prepared for whatever is inside killer bats swoop in luckly you have a bow do you:")
      print("1.kill all the bats")
      print("2.burn forest down")
      print("3.just leave the forest")
      choice = input("> ")
      if choice == "1":
           kill_bats()
      elif choice == "2":
           burn_forest()
      elif choice == "3":
           leave_forest()
      else:
        print("Invalid choice. Try again.")
        contin_forest()


def kill_bats():
      print("you kill all the bats and the villagers are so happy they make you the chief of the village")


def burn_forest():
      print("you brun down the forest and the whole village dies in the winter with no way to warm there homes")
      contin_forest()

def leave_forest():
      contin_drag()


def contin_drag():
      print("you continue on your journy you see buildings in the distance do you:")
      print("1.go castle")
      print("2.go cave")
      print("3.go abandon village")
      choice = input("> ")
      if choice == "1":
            go_cast()
      elif choice == "2":
           go_cave()
      elif choice == "3":
           go_abvi()
      else:
        print("Invalid choice. Try again.")
        go_villa()


def go_cast():
      print("you arive at the castle and get asked for the password to enter do you:")
      print("1.tell pasward")
      print("2.fight your way in")
      print("3.walk away")
      choice = input("> ")
      if choice == "1":
            tell_pass()
      elif choice == "2":
           fight_in()
      elif choice == "3":
            walk_away()
      else:
         print("Invalid choice. Try again.")
         contin_drag()

def tell_pass():
     print("1.macguy")
     print("2.macroon")
     print("3.toto")
     choice = input("> ")
     if choice == "1":
            macguy()
     elif choice == "2":
           macroon()
     elif choice == "3":
            toto()
     else:
         print("Invalid choice. Try again.")
         go_cast()

def macguy():
     print("nope try again")
     tell_pass()

def toto():
 print("nope try again")
 tell_pass()


def macroon():
     print("allright come on in what now:")
     print("1.take huge sword")
     print("2.leave to kill dragon ")
     choice = input("> ")
     if choice == "1":
            take_s()
     elif choice == "2":
           killdrag()
     else:
         print("Invalid choice. Try again.")
         go_cast()

def killdrag():
     print("the dragons scales are too hrad to cut through with your current sword")
     contin_drag()


def take_s():
     print("now you have everything you need")
     print("1.fight dragon")
     print("2.give up")
     choice = input("> ")
     if choice == "1":
            fig_dr()
     elif choice == "2":
           give_up()
     else:
         print("Invalid choice. Try again.")
         go_cast()

def fig_dr():
     print("you kill the dragon THE END")
     
def give_up():
      print("try again coward")



def fight_in():
     print("6 gaurds men rush out and you are exicuted")
     go_cast()
     

def walk_away():
     contin_drag()







def go_cave():
      print("you find a brown bear in the cave protecting its cubs do you:")
      print("1.fight the bear")
      print("2.RUN")
      choice = input("> ")
      if choice == "1":
            fight_bear()
      elif choice == "2":
           run_bear()
      else:
        print("Invalid choice. Try again.")
        contin_drag()

def fight_bear():
     print("you sucsesfully kill the bear and notice somthing in the back of the cave")
     print("1.investigate")
     print("2.leave with the bear fur")
     choice = input("> ")
     if choice == "1":
            invest_gate()
     elif choice == "2":
           lv_fur()
     else:
        print("Invalid choice. Try again.")
        go_cave()


def invest_gate():
      print("you find a battle axe and leave your sword")
      take_s()
def lv_fur():
     print("you leave with a cool bear skin cape and go fight the dragon")
     killdrag()

def run_bear():
     print("you make it out the cave safely where to next")
     print("1.go castle")
     print("2.go abandon village")
     choice = input("> ")
     if choice == "1":
            go_cast()
     elif choice == "2":
           go_abvi()
     else:
        print("Invalid choice. Try again.")
        go_cave()



def go_abvi():
      print("you walk through the village somthing seems off do you:")
      print("1.leave")
      print("2.explore and set up camp")
      choice = input("> ")
      if choice == "1":
            leave_avilla()
      elif choice == "2":
           ex_sup()
      else:
        print("Invalid choice. Try again.")
        contin_drag()


def leave_avilla():
     print("you deside it would be safer somewhere else")
     contin_drag()


def ex_sup():
     print("you get eaten in your sleep by the moose man")
     contin_drag()




start_adventure()