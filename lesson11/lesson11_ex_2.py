# 2. Write a Python function to check whether a number is in a given range.

def is_number_in_range(num, start, end):
    return start < num < end
print(is_number_in_range(2,4, 89))
print(is_number_in_range(8,4, 89))
