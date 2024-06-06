# Exercise 4:
# Write a Python program that generates a random number between 1 and 100 and asks
# the user to guess the number. The program should give hints whether the guessed
# number is too high or too low until the correct number is guessed.


import random
random_number = random.randint(1, 100)
guess = 0
while guess != random_number:
    guess = int(input("Please,guess the number:"))
    if  guess < random_number:
        print("Too low.Try again,please!")
    elif    guess > random_number:
        print("Too high.Try again,please!")
    else:
        print("Congratulations! You guessed the number correctly!")







