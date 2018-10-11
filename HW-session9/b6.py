district = ['ST', 'BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
population = [150300, 247100, 333300, 266800, 420900, 318000]

for i in range(len(population)):
    print(district[i] ,':', population[i])

area = [11743,9224,4335,1204,996,1009]
density = []

for x in range(len(area)):
    density.append((population[x])//(area[x]) )
    
print(density)
print("Average population density:",sum(density)//6)

    
  


