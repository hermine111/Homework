# 4.Write a python function which create dict from 2
# lists with the same length


def dict_from_lists(keys, values):
    if len(keys) != len(values):
        print("Lists must have the same length")

    result_dict = {}
    for i in range(len(keys)):
        result_dict[keys[i]] = values[i]
    return result_dict


print(dict_from_lists(["apple", "peach", "plum"], [5, 7, 8]))

