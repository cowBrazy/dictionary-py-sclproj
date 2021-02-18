D = {
    'Nom': 'Mahmoudi',
    'Prenom': 'Moun',
    'Age': 35
    }

#1
D['Prenom'] = 'Mouna'

#2
for key in D.keys():
    print(f'{key}\n')

print('----------------')

#3
for value in D.values():
    print(f'{value}\n')

print('----------------')

#4
for key, value in D.items():
    print(f'{key}\n')
    print(f'{value}\n')

print('----------------')

#5
Nom = D['Nom']
Prenom = D['Prenom']
Age = D['Age']

print(f'{Nom} {Prenom} a {Age} ans')
