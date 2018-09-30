str = "Please enter ur password"

while True:
    str = input("Please enter ur password")
    if (str.isdigit()) is not True:
        print("Welcome back")
        break
    else:
        print("Ur password must contain both letters and numbers")