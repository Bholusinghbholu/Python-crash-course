#extended in 6.11.py
cities = {
    'Delhi': {
        'country': 'India',
        'population': '32 million',
        'fact': 'Home of the Red Fort.',
        'area': '1,484 km²',
        'timezone': 'IST',
    },
    'Paris': {
        'country': 'France',
        'population': '11 million',
        'fact': 'City of Light.',
        'area': '105 km²',
        'timezone': 'CET',
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '37 million',
        'fact': 'Busiest station in the world.',
        'area': '2,194 km²',
        'timezone': 'JST',
    },
}

for city, info in cities.items():
    print(f"\n{city}:")
    for key, value in info.items():
        print(f"  {key.title()}: {value}")
