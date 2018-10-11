number = input("Enter a list of numbers")
list_number_typestr = number.split(",")
print(list_number_typestr)
list_number_typeInt = []
for number_str in list_number_typestr:
    list_number_typeInt.append(int(number_str))

print(list_number_typeInt)

print(*list_number_typeInt,sep=" ")
s = sum(list_number_typeInt)
print("sum of all entered number: ", s)




# user_pick = int(input("Enter a number")) #b7
# if user_pick in Intergers:
#     print("Found,Position:",user_pick)
# else:
#     print("Not found in our list:")

# Sum = sum(Intergers)  #b8
# print(Sum)

# print(69+96+56+89+-49+-345)

