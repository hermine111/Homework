# 2.Letters Count
# Write a Python function to calculate count of each letter in string
# Sample Input Sample Output
# count_letters(‘abrakadabra’)
# {a: 5, b: 2, r: 2, k: 1, d: 1}


def count_of_each_letter(string_ex):
    dict = {}
    for l in string_ex:
        if l in string_ex:
            keys = dict.keys()
            if l in keys:
                dict[l] += 1
            else:   dict[l] = 1
    return dict
print(count_of_each_letter("SUCCESS IS THE SUM OF SMALL EFFORTS!"))



