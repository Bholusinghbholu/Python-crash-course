#i used both 7.5 7.4
"""
prompt = "\nplease enter pizza topings"
prompt += "\n type 'quit' to quit :"
pizza_toppings =""
while pizza_toppings != "quit":
    pizza_toppings = input(prompt)

    if pizza_toppings != "quit":
        print(f"\nI will add {pizza_toppings} to your pizza")
        
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
    
prompt = "enter your age \n enter 'quit' to quit :"

while True:
    age  = input(prompt)
    if age.lower() == "quit":
        break
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free")
        elif 3 <= age <= 12:
            print("your ticket price is $10")
        else:
            print("your ticket price is $15")
    
"""
