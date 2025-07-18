#solution of exercise 5.5
age = 25  #set age=25

if (age<2):  #check if you are below 2
    print("you are a baby")

elif (2<=age<4): #check if you are b/w 2 and 4
    print("you are a toodler")

elif (4<=age<13):  #check if you are b/w 4 and 13
    print("you are a kid")

elif (13<=age<20):  #check if you are b/w 13 and 20
    print("you are a teenager")

elif (20<=age<65):  #check if you are b/w 20 and 65
    print("you are an adult")

else:  #if condition was false above
    print("you are an elder")
