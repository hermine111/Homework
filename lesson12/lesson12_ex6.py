# Exercise 6:
# Remove Duplicates from List.
# Write a function that takes a list of integers as input and returns a new list with duplicates
# removed, maintaining the original order of elements.


def remove_duplicates_from_list(list_ex):
    list_res = []
    for x in list_ex:
        if x not in list_res:
            list_res.append(x)
    return list_res
print(remove_duplicates_from_list([12, 5, 8, 8,7,9,8]))

