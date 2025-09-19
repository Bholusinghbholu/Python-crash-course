favorite_numbers = {
    'Ravi': [3, 7, 21],
    'Asha': [2, 5],
    'Kunal': [8],
}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(f"  {number}")
