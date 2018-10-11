number = input("Enter a list of number")
number_str = number.split(",")
number_int =[]
for x in number_str:
    number_int.append(int(x))

print("List of numbers:",*number_int,sep=", ")

for i in number_int:
    if i % 2 != 0:
        number_int.remove(i)

print("all even numbers are:",*number_int,sep=", ")

