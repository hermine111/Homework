# Exercise 5:
#Count Vowels and Consonants. Use isalpha() {}
#Write a function that takes a string as input and returns a dictionary with two keys, "vowels" and
#"consonants". The value for each key should be the count of vowels and consonants in the input
#string respectively.

def dict_with_two_keys_from_a_string(string_ex):
    result = {"vowels" : 0, "consonants": 0}
    vowels = {"a", "e", "u", "i", "w", "y"}
    for i in string_ex:
        if i.isalpha():
            if i in vowels:
                result["vowels"] += 1
            else:
                result["consonants"] += 1
    return result
print(dict_with_two_keys_from_a_string("My heart is in the highlands"))








