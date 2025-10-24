def fortune (lucky, magical, years):
    try:
        random = lucky*magical*years
    except:
        print("")
    
fortune (int(input("Enter your lucky number\n>")),float(input("Enter a magical multiplier")),float(input("Enter the amount of years you want to see into the future\n>")))
