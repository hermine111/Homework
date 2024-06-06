# 13. Sets Exercise:
# Write a function that checks if two sets are disjoint (have no common elements).


def are_disjoint(set1, set2):

    for element in set1:
        if element in set2:
            return False
    return True


print(are_disjoint({4, 5, 8, 7}, {9, 6, 2, 12}))

