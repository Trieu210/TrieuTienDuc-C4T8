str = "Please enter ur password"

while True:
    password = input("Please enter ur password")
    passlength = len(password)
    if len(password) > 8 and (str.isdigit())  is not True:
        print("Welcome back")
        break
    else:
        print("Ur password must contain both letters, numbers, and at least 8 charaters, and upper case letter ")

    