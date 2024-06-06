# Exercise 2:
# Write a Python program that asks the user to enter a password. Keep asking for the
# password until the correct password "secret" is entered. Provide appropriate feedback
# to the user.

correct_password = "secret"
while True:
    password = input("Please,enter the password: ")
    if password == correct_password:
        print("Welcome! You've entered the correct password.")
        break
    else:
        print("Incorrect password. Please try again.")

