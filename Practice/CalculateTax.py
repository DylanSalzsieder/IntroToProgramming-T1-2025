def calculate_tax(item, price, rate):
    print("The price of " + item + " is $" + str(round(float(price) * 1 + float(rate), 2)) + " after tax")


calculate_tax(input("Item name\n>"), input("Price of item\n>"), 0.06875)


