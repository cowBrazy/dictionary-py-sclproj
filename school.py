D = {
    'Nom': 'Mahmoudi',
    'Prenom': 'Moun',
    'Age': 35
    }
#1
D['Prenom'] = 'Mouna'

#2
for key in D.keys():
    print(key)

#3
for value in D.values():
    print(value)

#4
for key, value in D.items():
    print(key, value)

#5
print(f'{D["Nom"]} {D["Prenom"]} a {D["Age"]} ans')
