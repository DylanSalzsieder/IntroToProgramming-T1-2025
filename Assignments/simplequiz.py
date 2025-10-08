score = 0

def tallyscore(x, y):
    global score
    if x == y:
        print("Correct")
        score = score + 1
    else:
        print("Incorrect")



tallyscore(input("What is 2 + 2?\n>"), "4")
tallyscore(input("What color is the sky?\n>"), "blue")
tallyscore(input("What is the biggest state in the US?\n>"), "alaska")
tallyscore(input("What is 5 squared?\n>"), "25")
tallyscore(input("What year is it?\n>"), "2025")

print("You got " + str(score) + "/5")