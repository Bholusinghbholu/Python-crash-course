sandwich_orders = ['tuna sandwhich','club sandwhich','pav sandwhich','samosa sandwhich','paneer sandwhich',]
finished_sandwhiches = []

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
