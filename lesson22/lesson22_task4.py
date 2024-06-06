# 4. List Exercise:
# Write a function that takes two lists and returns a new list containing only the common
# elements. (without using set)

def lists_containing_common_elements(list1,list2):
    res_list = []
    for i in list1:
        if i in list2:
            res_list.append(i)
    return res_list

print(lists_containing_common_elements([4,8,7,5,9], [5,8,6,3,9]))
