#1. String Length Checker
# Write a function that checks the length of a string provided by the user. Handle the
# TypeError by raising a custom exception if the input is not a string.

def string_length_checker(x):
    if isinstance(x, str):
        return len(x)
    else:
        raise TypeError("The input is not a string.")


print(string_length_checker(4))




