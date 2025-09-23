sandwich_orders = ['pastrami','tuna sandwhich','club sandwhich','pav sandwhich','pastrami','samosa sandwhich','paneer sandwhich','pastrami']
finished_sandwhiches = []
print("The deli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while True:
    if len(sandwich_orders) == 0:
        break
    else:
        cooking = sandwich_orders.pop()
        print(f"I made your {cooking.title()}")
        finished_sandwhiches.append(cooking)

print("\nI have made folloing sandwhiches :")
for finished_sandwhich in finished_sandwhiches:
    print(finished_sandwhich)
