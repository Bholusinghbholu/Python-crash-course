pet1 = {'animal': 'dog', 'owner': 'Sonia'}
pet2 = {'animal': 'parrot', 'owner': 'Vikas'}
pet3 = {'animal': 'cat', 'owner': 'Pooja'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"{pet['owner']} has a {pet['animal']}.")
