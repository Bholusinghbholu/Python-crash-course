prompt = "enter your age \n enter 'quit' to quit :"
active = True
while active:
    age  = input(prompt)
    if age.lower() == "quit":
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free")
        elif 3 <= age <= 12:
            print("your ticket price is $10")
        else:
            print("your ticket price is $15")
    
