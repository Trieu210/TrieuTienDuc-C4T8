color = ['blue', ' green', 'yellow', 'red']
# print("our color list:")
# print(*color,sep=", ")

# new = str(input("Enter a color"))
# print("our new color list:")
# color.append(new)
# print(*color,sep=", ")

# ps = int(input("Enter a position:"))
# print("color at position:",ps)
# print(color[ps])

 for i, color in enumerate(color):
    print(i +1,".",color)

delete0 = input("Item to delete:")
print(color)
if delete0.isdigit():
    color.pop(int(delete0))
    for i,color in enumerate(color):
        print(i +1,".",color)
else:
    color.remove(delete0)
    print(color)
    for i,color in enumerate(color):
        print(i +1,".",color)
    




