# Filtering Word Lengths:
# ○ Given a list of words, create a dictionary where keys are words, and values are
# their lengths, but only for words with lengths greater than 3.

my_lst = ["January", "February", "March", "April", "May"]
my_dict = {word: len(word) for word in my_lst if len(word) > 3}
print(my_dict)

