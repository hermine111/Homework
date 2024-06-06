# 1.Max of Three
# Write a Python function to find the Max of three numbers.
# Sample Input Sample Output
# max_of_three(5, 11, 3)
# 11


def  max_of_three_numbers(x, y, z):
    if x >= y and x >= z:
        largest = x
    elif    y >= x and y >= z:
        largest = y
    else:
        largest = z
    return largest
print(max_of_three_numbers(50,10,77))





