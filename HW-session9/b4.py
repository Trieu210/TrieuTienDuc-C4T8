entered_list = [5,1,4,68,46,57,6] 

for i in entered_list:
    if i % 2 != 0:
        entered_list.remove(i)

print("All even numbers :" ,entered_list)
