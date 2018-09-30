str = "Please enter ur username"
while True:
    str = input("Please enter ur username")
    if (str.isalpha() )is True:
        print("Welcome user")
        break
    else:
        print("Username must be letters only")
