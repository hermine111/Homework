#2. List Element Removal
#Write a function that removes an element at a specified index from a list. Handle the
#IndexError by raising a custom exception if the index is out of range.


def remove_element_at_specified_index(list_ex, index_):
    if index_ in list_ex:
        list_ex.pop(index_)
        return list_ex
    elif index_ < len(list_ex):
        raise IndexError("The index is out of range")
    return IndexError


print((remove_element_at_specified_index([1,2,8,6,2],7)))


