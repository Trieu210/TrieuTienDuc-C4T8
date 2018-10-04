x = input("pls enter the month u like")

if x in ["February"]:
    print("No.of days:28/29 days")
elif x in  ["April" , "June","September","November"]:
    print("No.of days:30 days") 
elif x in  ["January","March","May","July","August","October","December"]:
    print("No.of days:31 days")
else:
    print("NA")