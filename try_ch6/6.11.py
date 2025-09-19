cities = {
    'Delhi': {
        'country': 'India',
        'population': '32 million',
        'fact': 'Home of the Red Fort.'
    },
    'Paris': {
        'country': 'France',
        'population': '11 million',
        'fact': 'Known as the City of Light.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '37 million',
        'fact': 'Has the busiest train station in the world.'
    },
}

for city, info in cities.items():
    print(f"\n{city}:")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}")
