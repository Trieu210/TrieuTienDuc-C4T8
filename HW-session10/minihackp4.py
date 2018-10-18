price = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 12000,
    'ASUS': 400,
    'TOSHIBA': 600,
    'FUJITSU': 900,
}

computers ={
    'HP':20,
    'DELL':50,
    'MACBOOK':12,
    'ASUS':30,
    'TOSHIBA':15,
    'FUJITSU':15,
}
total1 = []
for k in computers and price:
    total = computers[k] * price[k]
    print('Price of ', k ,":", total)
    total1.append(total)

print(total1)

sum_total = sum(total1)
print(sum_total)

