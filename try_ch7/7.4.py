prompt = "\nplease enter pizza topings"
prompt += "\n type 'quit' to quit :"
pizza_toppings =""
while pizza_toppings != "quit":
    pizza_toppings = input(prompt)

    if pizza_toppings != "quit":
        print(f"\nI will add {pizza_toppings} to your pizza")
        
