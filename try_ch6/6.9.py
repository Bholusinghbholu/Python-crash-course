favorite_places = {
    'Amit': ['Goa', 'Paris', 'Shimla'],
    'Suman': ['Kerala'],
    'Ravi': ['New York', 'London']
}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places are:")
    for place in places:
        print(f"- {place}")
