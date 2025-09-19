person1 = {'first_name': 'Ravi', 'last_name': 'Sharma', 'age': 28, 'city': 'Delhi'}
person2 = {'first_name': 'Anita', 'last_name': 'Patel', 'age': 32, 'city': 'Mumbai'}
person3 = {'first_name': 'Rahul', 'last_name': 'Verma', 'age': 25, 'city': 'Jaipur'}

people = [person1, person2, person3]

for person in people:
    print(f"{person['first_name']} {person['last_name']} is {person['age']} "
          f"years old and lives in {person['city']}.")
