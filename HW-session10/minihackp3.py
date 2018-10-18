price = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 12000,
    'ASUS': 400,
    'ACER': 350,
    'TOSHIBA': 600,
    'FUJISU': 900,
    'ALIENWARE': 1000,
}

computers ={
    'HP':20,
    'DELL':50,
    'MACBOOK':12,
    'ASUS':30,
    'TOSHIBA':15,
    'FUJITSU':15,
}


print(price['ASUS'])

user = input("Enter a computer brand ").upper()

if user in computers:
    print(price[user])
    print('number of computers left:')
    print(computers[user])
    quantity = int(input("How many computers u want to buy"))
    print(price[user]*quantity)
else:
    print('Sr its not available')







