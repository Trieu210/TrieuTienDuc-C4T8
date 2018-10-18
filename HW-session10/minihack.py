computers ={
    'HP':20,
    'DELL':50,
    'MACBOOK':12,
    'ASUS':30,
}

user = input("Enter a computer brands").upper()       #part1
if user in computers:
    print(computers[user])

new = input('Enter a computer brand').upper()
computers[new] = 10
print(computers)

computers['DELL'] +=10
computers['MACBOOK']-=10
print(computers)


