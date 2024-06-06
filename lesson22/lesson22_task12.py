# 12. List Exercise:
# Write a function that returns the nth largest element from a list.

def nth_largest_element(list_ex, n):

    sorted_list = sorted(list_ex, reverse=True)
    if n <= len(sorted_list):
        return sorted_list[n - 1]
    else:
        return None


print(nth_largest_element([4566, 785, 451, 123], 2))
