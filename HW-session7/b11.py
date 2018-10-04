print("Welcome to Freaking Math")
while True:
    import random
    import math
    a = random.randint(1,100)
    b = random.randint(1,100)
    c = a + b + random.randint(-1,1)
    print(a , "+" ,b , "=" , c)
    d = str(input("True or False"))
    if c == a + b:
        if d == "True":
            print("Correct Answer")
        elif d == "False":
            print("Wrong Answer")
            print("Game Over")
            break
    if  c != a + b:
        if d == "True":
            print("Wrong answer")
            print("Game Over")
            break
        elif d == "False":
            print("Correct answer")
            
    
    


        
