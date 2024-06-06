# Exercise 6: Count Words Function
# Write a function that counts the number of words in a sentence.

"""
Parameters
string
returns
number
"""
def count_of_words(string_ex):
    count = len(string_ex.split())
    return count
print(count_of_words("Success is not final; failure is not fatal: It is the courage to continue that counts."))

