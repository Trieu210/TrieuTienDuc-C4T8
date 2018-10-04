x = input("Enter ur username")
while True:
    y = str(input("Enter ur password"))
    a = str(input("Pls re-enter ur password"))
    if len(a) == len(y) >= 8 and a.isalnum():
        z = str(input("Enter ur email"))
        if "@" not in z and ".com" not in z:
            print("Invalid email")
        else:
            print("Welcome", x)
            break
    else:
        print(" Password must be atleast 8 letters long")
        

        
