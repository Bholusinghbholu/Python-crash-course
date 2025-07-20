#solution exercise 5.8
#usernames names list
usernames = ["nikhil","nishant","admin","ayush","golu"]

if usernames:                       #checking if username is not empty
    for username in usernames:      #looping through list

        if username == "admin":      #special message for admin
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for login again.")
        
else:
    print("\nwe need to find some users")


# second version of this program 
#empty user name
usernames = []

if usernames:                       #checking if username is not empty
    for username in usernames:      #looping through list

        if username == "admin":      #special message for admin
            print(f"Hello {username}, would you like to see a ststus report?")
        else:
            print(f"Hello {username}, thank you for login again.")
        
else:
    print("\nwe need to find some users")
