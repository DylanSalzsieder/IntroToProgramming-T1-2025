password = "Knights25"

def ask_password():
    sub = input("Enter password\n>")
    if sub == password:
        print("Correct")
    else:
        print("Incorrect")
        ask_password()

ask_password()