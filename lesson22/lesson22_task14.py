# 14. Strings Exercise:
# Write a function that capitalizes the first letter of each word in a sentence.


def capitalize_first_letter(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)


print(capitalize_first_letter("Either you run the day or the day runs you."))
