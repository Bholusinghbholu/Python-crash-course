#solution of exercise 5.11
#list of numbers
ordinal_numbers = list(range(1,10))
for ordinal_number in ordinal_numbers:     #looping and cheking 
    if ordinal_number == 1:
        print(f"{ordinal_number}st")
    elif ordinal_number == 2:
        print(f"{ordinal_number}nd")
    elif ordinal_number == 3:
        print(f"{ordinal_number}rd")
    else:
        print(f"{ordinal_number}th")
        
