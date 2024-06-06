# Exercise 1: Check Pangram Function
# Write a function that checks if a sentence is a pangram.

"""
Parameters
string
returns
Boolean
"""


def is_pangram(string_sent):
    alphabet = [chr(i) for i in range(97, 123)]
    for letter in alphabet:
        if letter not in string_sent.lower():
            return False
    return True
print(is_pangram("A quick movement of the enemy will jeopardize six gunboats."))




