# 9. Dictionaries Exercise:
# Write a function that finds the key with the maximum value in a dictionary.


def find_key_with_max_value(dictionary_ex):
    max_key, max_value = list(dictionary_ex.items())[0]
    for k, v in dictionary_ex.items():
        if v > max_value:
            max_value = v
            max_key = k

    return max_key


print(find_key_with_max_value({"Anna": 90, "Jane": 70, "Sara": 100}))
