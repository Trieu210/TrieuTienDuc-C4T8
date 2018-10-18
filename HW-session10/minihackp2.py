computers ={
    'HP':20,
    'DELL':50,
    'MACBOOK':12,
    'ASUS':30,
}


for k in computers:                   #part2
    print(computers[k])               

total = sum(computers.values())
print(total)
  
computers['FUJITSU']=15
computers['ALIENWARE']=15
print(computers)


total = sum(computers.values())
print(total)
