player = {
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': ['Shield', 'Bread Loaf'],
    'Gold': 100,
    'Level': 2,

}

# player['Gold'] += 50
# player['Backpack'].append('Flintstone')
# print(player)

# player['Pocket'] = ['MonsterDex','Flashlight']
# print(player)

skill = [
    {
        'Skill1' : {
        'Name' : 'Tackle',
        'Minimum level' : 1,
        'Damage': 5,
        'Hit rate': 0.3,
        },
    },
    {
        'Skill2' : {
            'Name' : 'Quick attack',
            'Minimum level' : 2,
            'Damage' : 3,
            'Hit rate' : 0.5,
        },
    },
    {
        'Skill3' : {
            'Name' : 'Strong Kick',
            'Minimum level' : 4,
            'Damage' : 7,
            'Hit rate' : 0.2,
        }
    }
]

for i in skill:
    for key,value in i.items():
        print(key,":",value)
        for key1,value1 in value.items():
            print(key1,":",value1)
        print("_______")

import random
combat = random.choice(skill)
print(combat)
print("This is the skill u can use in combat")

if 'Skill1' in combat:
    print("Total Damage:",skill[0]['Skill1']['Damage'])
elif 'Skill2' in combat:
    print("Total Damage:",skill[1]['Skill2']['Damage'])
elif 'Skill3' in combat:
    print("Your lv is too low")






    
    