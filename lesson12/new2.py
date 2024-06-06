#  Exercise 2:
# List Manipulation Write a Python function called remove_duplicates that takes a list as an
# argument and returns a new list with duplicates removed.


def remove_duplicates(input_list):
    elements_ = set(input_list)
    return list(elements_)


print(remove_duplicates([45, 87, 55, 45]))



