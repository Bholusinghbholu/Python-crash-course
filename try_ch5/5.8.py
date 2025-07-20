#solution exercise 5.8
#usernames names list
usernames = ["nikhil","nishant","admin","ayush","golu"]

for username in usernames:      #looping through list

    if username == "admin":      #special message for admin
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for login again.")
        
