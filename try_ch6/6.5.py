
rivers ={
    "ganga":"india",
    "nile":"egypt",
    "amezon":"brazil",
}

for river,country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

#printing only names of river
for river in rivers:
    print(river)

#printing only country

for country in rivers.values():
    print(country)
     
    
