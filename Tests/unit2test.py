#1
word1 = input("Enter a word\n>")
word2 = input("Enter a second word\n>")
word3 = input("Enter a third word\n>")

print(word1 + word2 + word3)


#2
def add_three(x, y, z):
    print(int(x) + int(y) + int(z))
    
add_three(input("Enter an integer\n>"), input("Enter a second integer\n>"), input("Enter a third integer\n>"))


#3
def data_three():
    word = input("Enter a word\n>")
    integer = input("Enter an Integer\n>")
    flo = input("Enter a float\n>")
    print(str(int(integer) + float(flo)) + word)

data_three()