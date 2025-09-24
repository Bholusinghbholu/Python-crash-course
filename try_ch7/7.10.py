#polling program for cities
print("If you could visit one place in the world, where would you go?")

cities = ["Delhi", "Mumbai", "Kolkata", "Hampi"]

# votes lists
poll = []     # sab votes
null = []     # invalid votes
Delhi = []
Mumbai = []
Kolkata = []
Hampi = []

# display options
for i, city in enumerate(cities, start=1):
    print(f"{i}. {city}")

print("\n:: Enter your vote (1-4) or 'q' to quit ::")
active = True

#prompt loop
while active:
    current = input(": ")

    if current == "q" or current == "quit":
        print(f"\nTotal votes: {len(poll)}")
        print(f"Null votes: {len(null)}")
        print("\n--- Results ---")
        print(f"Delhi   : {len(Delhi)}")
        print(f"Mumbai  : {len(Mumbai)}")
        print(f"Kolkata : {len(Kolkata)}")
        print(f"Hampi   : {len(Hampi)}")
        active = False

    else:
#counting
        poll.append(current)

        if current == '1':
            Delhi.append(current)
        elif current == '2':
            Mumbai.append(current)
        elif current == '3':
            Kolkata.append(current)
        elif current == '4':
            Hampi.append(current)
        else:
            null.append(current)
#end

