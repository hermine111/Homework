# 4. Login System
# Write a simple login system where the user enters a username and password. Handle
# the KeyError by raising a custom exception if the username is not found in the users
# database(dictionary).




users_database = {"Harry": "456","Jane":"5784"}
user_name = input("Enter your username,please! ")
pass_word = input("Enter your password,please! ")
if user_name in users_database and pass_word == users_database[user_name]:
    print("Login successful!")
else:
    raise KeyError("User doesn't exist or wrong password")




