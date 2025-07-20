#solution of exercise 5.10
#list of current users
current_users = ["ramesh","mahesh","Mukesh","suresh","aditya","ayush"]

#new users
new_users = ["nishant","kush","Ramesh","abhinav","mukesh"]

#making them unique
current_users_lower = [current_user.lower() for current_user in current_users]

for new_user in new_users:                 #looping new users 
    if new_user.lower() in current_users_lower:
        print("the person will need to enter a new username")
    else:
        print("username is availabe")
